# -*- coding: utf-8 -*-

import uuid
from http import HTTPStatus

__all__ = (
    'Handler',
)


class Handler(object):
    def __init__(self, urlpart, status=HTTPStatus.OK, headers=None, body=None):
        self.uid = uuid.uuid4().hex
        self.urlpart = urlpart
        self.status = status
        self.headers = headers or {}
        self.body = body or {}
