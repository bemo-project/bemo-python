# -*- coding: utf-8 -*-

from bemo import handlers, templates

__all__ = (
    'Session',
)


XHOOK_SCRIPT_URL = '//cdn.rawgit.com/jpillora/xhook/1.3.5/dist/xhook.min.js'


class Session(object):
    """
    Base `bemo` session class.

    Should be used as entry point to work with XHook.
    Session class contains all needed methods to create, inject and release
    handlers. The best way to use this class as context manager, but if you
    want you can use this class in classic way.
    """
    def __init__(self, wd=None, xhook_script_url=XHOOK_SCRIPT_URL):
        """
        Initializes session.

        :param wd: Web driver
        :param xhook_script_url: URL to XHook script
        """
        self._wd = wd
        self._xhook_script_url = xhook_script_url
        self._xhook_handlers = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.release()

    def handle(self, urlpart, **kwargs):
        handler = handlers.Handler(urlpart, **kwargs)
        self.add_handler(handler)

        return handler

    def add_handler(self, handler):
        # Inject web driver into handler to make possibility to work with
        # asserts. And, yes, I know this is not good idea, but ¯\_(ツ)_/¯
        handler._wd = self._wd

        self._xhook_handlers.append(handler)

    def inject(self):
        script = self._wd.execute_script

        script(templates.xhook__initialize({
            'XHookScriptURL': self._xhook_script_url,
        }))
        script(templates.xhook__handlers({
            'handlers': self._xhook_handlers,
        }))
        script(templates.xhook__enable())

    def release(self):
        script = self._wd.execute_script

        script(templates.xhook__release())
