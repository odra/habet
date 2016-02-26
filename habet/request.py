  # -*- encoding: utf-8 -*-
import urlparse


class Request(object):
  def __init__(self, **kwags):
    self.method = kwags.get('method')
    self.path = kwags.get('path')
    self.body = kwags.get('body')
    self.headers = kwags.get('headers', {})
    self.params = kwags.get('params', {})
    self.query_string = kwags.get('query_string')
    self.args = {}
    self.content_type = kwags.get('content_type')
    self.content_length = kwags.get('content_length', 0)

  def read_body(self):
    if self.body is not None:
      self.body = self.body.read()

  def parse_headers(self):
    headers = {}
    for item in self.headers:
      _item = item.replace('HTTP_', '').replace('_', '-')
      headers[_item] = self.headers[item]
    self.headers = headers

  def parse_query_string(self):
    self.args = {i[0]:i[1] for i in urlparse.parse_qsl(self.query_string)}

  def parse_params(self):
    self.params = {k:str(self.params[k]) for k in self.params}
