# -*- coding: utf-8 -*-

import uuid
from http import HTTPStatus

from bemo import functional, templates

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

        self._wd = None

    def assert_call_count(self, expected):
        assert self._call_count() == expected

    def assert_called(self):
        assert self._call_count()

    def assert_called_with(self, expected):
        calls = self._calls()

        assert len(calls) == len(expected)

        for i in range(len(calls)):
            assert functional.partial_match(calls[i], expected[i])

    def assert_called_once_with(self, expected):
        calls = self._calls()

        assert len(calls) == 1
        assert functional.partial_match(calls[0], expected)

    def _call_count(self):
        script = self._wd.execute_script

        return script(templates.asserts__call_count({
            'handler': self,
        }))

    def _calls(self):
        script = self._wd.execute_script

        return script(templates.asserts__calls({
            'handler': self,
        }))
