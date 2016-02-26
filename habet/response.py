# -*- encoding: utf-8 -*-
import httplib
import json


DEFAULT_PARSER = json.dumps


class Response(object):
  def __init__(self, status=200, headers={}, body=None, parser=None):
    self._status = status
    self._reason = self.get_reason(self.status)
    self.headers = headers
    self._body = body
    self.parser = parser

  def get_response_headers(self):
    return [(k, self.headers[k]) for k in self.headers]

  @property
  def body(self):
    if self._body:
      if self.parser is not None:
        return self.parser(self._body)
      return DEFAULT_PARSER(self._body)
    return ''

  @body.setter
  def body(self, body):
    self._body = body

  @property
  def status(self):
    return self._status

  @status.setter
  def status(self, status_code):
    self.status = status
    self._reason = self.get_reason(status_code)

  @property
  def reason(self):
    return self._reason

  def get_reason(self, status_code):
    return httplib.responses.get(status_code)
