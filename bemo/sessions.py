# -*- coding: utf-8 -*-

from bemo import templates

__all__ = (
    'Session',
)


XHOOK_SCRIPT_URL = '//cdn.rawgit.com/jpillora/xhook/1.3.5/dist/xhook.min.js'


class Session(object):
    def __init__(self, wd=None, xhook_script_url=XHOOK_SCRIPT_URL):
        """
        Initializez session.

        :param wd: Web driver
        :param xhook_script_url: URL to XHook script
        """
        self._wd = wd
        self._xhook_script_url = xhook_script_url

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.disable()

    def handle(self):
        pass

    def inject(self):
        script = self._wd.execute_script

        script(templates.xhook__initialize({
            'XHookScriptURL': self._xhook_script_url,
        }))
        script(templates.xhook__enable())

    enable = inject

    def disable(self):
        script = self._wd.execute_script

        script(templates.xhook__disable())
