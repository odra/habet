# -*- encoding: utf-8 -*-
import sys
sys.path.append('../')
from habet import Application, Response, Handler


class RootHandler(Handler):
  def get(self):
    return Response(body={'action': 'new'})


class NameHandler(Handler):
  def set_default_headers(self):
    self.default_headers = {
      'X-Custom-Header': 'My header',
      'Content-Type': 'application/json'
    }
  
  def get(self):
    return Response(body={'name': self.request.params['name']})

  def finish(self):
    print app.some_var
    print 'log stuff'


app = Application(some_var='my var')
app.route('/', RootHandler)
app.route('/{name}', NameHandler)


if __name__ == '__main__':
  app.listen()
