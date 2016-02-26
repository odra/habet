# -*- encoding: utf-8 -*-
from habet.response import Response


class BaseServerError(Exception):
  def __init__(self):
    self.status = None
    self.code = None
    self.message = None
    self.data = None
    self.content_type = 'application/json'

  def as_response(self):
    body = {
      'error': {
        'code': self.code,
        'message': self.message,
        'data': self.data
      }
    }
    headers = {
      'Content-Type': self.content_type
    }
    return Response(status=self.status, headers=headers, body=body)


class MethodNotAllowedError(BaseServerError):
  def __init__(self, method=None, path=None):
    super(MethodNotAllowedError, self).__init__()
    self.status = 405
    self.code = -32000
    self.message = 'Method not allowed.'
    self.data = {
      'method': method,
      'path': path
    }


class UnauthorizedError(BaseServerError):
  def __init__(self, method=None, path=None):
    super(UnauthorizedError, self).__init__()
    self.status = 401
    self.code = -32001
    self.message = 'Unauthorized.'
    self.data = {
      'method': method,
      'path': path
    }


class ForbiddenError(BaseServerError):
  def __init__(self, method=None, path=None):
    super(ForbiddenError, self).__init__()
    self.status = 403
    self.code = -32002
    self.message = 'Forbidden.'
    self.data = {
      'method': method,
      'path': path
    }


class NotFoundError(BaseServerError):
  def __init__(self, method=None, path=None):
    super(NotFoundError, self).__init__()
    self.status = 404
    self.code = -32004
    self.message = 'Resource/path not found.'
    self.data = {
      'method': method,
      'path': path
    }


class InternalError(BaseServerError):
  def __init__(self, method=None, path=None):
    super(InternalError, self).__init__()
    self.status = 500
    self.code = -32099
    self.message = 'Internal/Unknown server error.'
    self.data = {
      'method': method,
      'path': path
    }
