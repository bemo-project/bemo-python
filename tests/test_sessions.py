# -*- coding: utf-8 -*-

from unittest.mock import MagicMock

from bemo import sessions


def test_session():
    wd_mock = MagicMock()

    with sessions.Session(wd=wd_mock) as session:
        handler = session.handle('handler')

        assert len(session._xhook_handlers) == 1
        assert handler._wd == wd_mock

        # just run code to check that everything ok
        session.inject()
