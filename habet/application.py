# -*- encoding: utf-8 -*-
from gevent import wsgi, monkey
monkey.patch_all()
import gevent
from routes import Mapper
from habet import errors


class Application(object):
  def __init__(self, **kwargs):
    self.routes = Mapper()
    {setattr(self, i, kwargs[i]) for i in kwargs}

  def __call__(self, environ, start_response):
    return self.application(environ, start_response)

  def route(self, path, handler, **kwargs):
    name = kwargs.get('name', handler.__class__.__name__)
    self.routes.connect(name, path, controller=handler)

  def application(self, environ, start_response):
    route = self.routes.match(environ['PATH_INFO'])
    try:
      handler = route['controller'](environ,
        {k:v for k,v in route.iteritems() if k != 'controller'})
    except TypeError:
      res = errors.NotFoundError(environ['REQUEST_METHOD'],
        environ['PATH_INFO']).as_response()
      start_response('%s %s' % (res.status, res.reason), res.get_response_headers())
      return [res.body]
    handler.start()
    try:
      res = getattr(handler, environ['REQUEST_METHOD'].lower())()
    except errors.BaseServerError as e:
      res = e.as_response()
    handler.set_default_headers()
    res.headers.update(**handler.default_headers)
    start_response('%s %s' % (res.status, res.reason), res.get_response_headers())
    gevent.spawn(handler.finish)
    return [res.body]

  def listen(self, host='127.0.0.1', port=5000, debug=True, log=None):
    addr = (host, port)
    wsgi.WSGIServer(addr, self.application, log=log).serve_forever()
