# -*- coding: utf-8 -*-

import uuid

try:
    from http import HTTPStatus
except ImportError:
    from httpstatus import HTTPStatus

from bemo import functional, templates

__all__ = (
    'Handler',
)


class Handler(object):
    """
    Base `bemo` handler class.

    Should be used to inject into JS code.
    Handler class contains all data to build XHook response.
    All assertiona should be used after injection in JS code.
    """
    def __init__(self, urlpart, status=HTTPStatus.OK, headers=None, body=None):
        """
        Initializes handelr.

        :param urlpart: Part of URL to handle
        :param status: HTTP status code, must be instance of `http.HTTPStatus`
        :param headers: HTTP headers
        :param body: response body, must be JSON serializable
        """
        self.uid = uuid.uuid4().hex
        self.urlpart = urlpart
        self.status = status
        self.headers = headers or {}
        self.body = body or {}

        self._wd = None

    def assert_not_called(self):
        """
        Assert that the handler was never called.
        """
        call_count = self._call_count()
        if call_count:
            raise AssertionError('Expected handler ({urlpart}) to not have'
                                 ' been called. Called {count} times.'
                                 .format(urlpart=self.urlpart,
                                         count=call_count))

    def assert_called(self):
        """
        Assert that the handler was called at least once.
        """
        call_count = self._call_count()
        if not call_count:
            raise AssertionError('Expected handler ({urlpart}) to have been'
                                 ' called.'.format(urlpart=self.urlpart))

    def assert_called_once(self):
        """
        Assert that the handler was called only once.
        """
        call_count = self._call_count()
        if call_count != 1:
            raise AssertionError('Expected handler ({urlpart}) to have been'
                                 ' called once. Called {count} times.'
                                 .format(urlpart=self.urlpart,
                                         count=call_count))

    def assert_call_count(self, expected):
        """
        Assert that the handler was called the specified number of times.
        """
        call_count = self._call_count()
        if call_count != expected:
            raise AssertionError('Expected handler ({urlpart}) to not have'
                                 ' been called expected {expected} number'
                                 ' of times. Called {count} times.'
                                 .format(urlpart=self.urlpart,
                                         expected=expected, count=call_count))

    def assert_called_with(self, expected):
        """
        Assert that the handler was called with the specified requests.
        """
        calls = self._calls()

        call_count = len(calls)
        expected_count = len(expected)
        if call_count != expected_count:
            raise AssertionError('Expected handler ({urlpart}) to not have'
                                 ' been called expected {expected} number'
                                 ' of times. Called {count} times.'
                                 .format(urlpart=self.urlpart,
                                         expected=expected_count,
                                         count=call_count))

        for i in range(len(calls)):
            if not functional.partial_match(calls[i], expected[i]):
                raise AssertionError('Expected handler ({urlpart}) to not have'
                                     ' been called with expected ({expected})'
                                     ' request. Called with ({called})'
                                     .format(urlpart=self.urlpart,
                                             expected=expected[i],
                                             called=calls[i]))

    def assert_called_once_with(self, expected):
        calls = self._calls()

        call_count = len(calls)
        if call_count != 1:
            raise AssertionError('Expected handler ({urlpart}) to have been'
                                 ' called once. Called {count} times.'
                                 .format(urlpart=self.urlpart,
                                         count=call_count))

        if not functional.partial_match(calls[0], expected):
            raise AssertionError('Expected handler ({urlpart}) to not have'
                                 ' been called with expected ({expected})'
                                 ' request. Called with ({called})'
                                 .format(urlpart=self.urlpart,
                                         expected=expected,
                                         called=calls[0]))

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
