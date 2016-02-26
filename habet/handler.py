# -*- encoding: utf-8 -*-
from habet.response import Response
from habet.request import Request
from habet import errors


class Handler(object):
  def __init__(self, env, params={}):
    self.request = Request(path=env['PATH_INFO'],
      method=env['REQUEST_METHOD'],
      query_string=env['QUERY_STRING'],
      content_type=env.get('CONTENT_TYPE'),
      content_length=env.get('CONTENT_LENGTH', 0),
      headers={k:v for k,v in env.iteritems() if k.startswith('HTTP_')},
      params=params,
      body=env.get('wsgi.input'))
    self.default_headers = {}
  
  def set_default_headers(self):
    pass

  def start(self):
    self.request.read_body()
    self.request.parse_headers()
    self.request.parse_query_string()
    self.request.parse_params()

  def finish(self):
    pass

  def post(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def get(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def put(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def delete(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def options(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def head(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def trace(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)

  def connect(self):
    raise errors.MethodNotAllowedError(self.request.method, self.request.path)
