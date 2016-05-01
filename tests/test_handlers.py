# -*- coding: utf-8 -*-

from unittest.mock import MagicMock

import pytest

from bemo import handlers


def test_assert_not_called():
    wd_mock = MagicMock()
    wd_mock.execute_script.return_value = 0

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    handler.assert_not_called()

    wd_mock.execute_script.return_value = 1
    with pytest.raises(AssertionError):
        handler.assert_not_called()


def test_assert_called():
    wd_mock = MagicMock()
    wd_mock.execute_script.return_value = 1

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    handler.assert_called()

    wd_mock.execute_script.return_value = 0
    with pytest.raises(AssertionError):
        handler.assert_called()


def test_assert_called_once():
    wd_mock = MagicMock()
    wd_mock.execute_script.return_value = 1

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    handler.assert_called_once()

    wd_mock.execute_script.return_value = 2
    with pytest.raises(AssertionError):
        handler.assert_called_once()


def test_assert_call_count():
    wd_mock = MagicMock()
    wd_mock.execute_script.return_value = 2

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    handler.assert_call_count(2)

    wd_mock.execute_script.return_value = 4
    with pytest.raises(AssertionError):
        handler.assert_call_count(2)


def test_assert_called_with():
    wd_mock = MagicMock()
    wd_mock.execute_script.return_value = [{
        'key': 'value',
    }]

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    with pytest.raises(AssertionError):
        handler.assert_called_with([])

    with pytest.raises(AssertionError):
        handler.assert_called_with([{
            'other_key': 'other_value',
        }])

    handler.assert_called_with([{
        'key': 'value',
    }])


def test_assert_called_once_with():
    wd_mock = MagicMock()

    handler = handlers.Handler('handler')
    handler._wd = wd_mock

    wd_mock.execute_script.return_value = [
        {
            'key': 'value',
        },
        {
            'key': 'value',
        },
    ]
    with pytest.raises(AssertionError):
        handler.assert_called_once_with({
            'key': 'value',
        })

    wd_mock.execute_script.return_value = [{
        'key': 'value',
    }]
    with pytest.raises(AssertionError):
        handler.assert_called_once_with({
            'other_key': 'other_value',
        })

    handler.assert_called_once_with({
        'key': 'value',
    })
