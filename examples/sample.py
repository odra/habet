# -*- encoding: utf-8 -*-
import sys
sys.path.append('../')
from habet import Application, Response, Handler, errors
import json


#custom error register
class InvalidJSONError(errors.BaseServerError):
  def __init__(self, *args, **kwargs):
    super(InvalidJSONError, self).__init__(*args, **kwargs)
    self.status = 400
    self.code = -32005
    self.message = 'Invalid JSON'


#root handler
class RootHandler(Handler):
  def get(self):
    return Response(body={'action': 'new'})


#name handler
class NameHandler(Handler):
  def set_default_headers(self):
    self.default_headers = {
      'X-Custom-Header': 'My header',
      'Content-Type': 'application/json'
    }
  
  def get(self):
    return Response(body={'name': self.request.params['name']})

  def post(self):
    try:
      body = json.loads(self.request.body)
    except (TypeError, ValueError):
      raise InvalidJSONError()
    return Response(body=body)    

  def finish(self):
    print app.some_var
    print 'log stuff'


#application setup
app = Application(some_var='my var')
app.route('/', RootHandler)
app.route('/{name}', NameHandler)


#run app
if __name__ == '__main__':
  app.listen()
