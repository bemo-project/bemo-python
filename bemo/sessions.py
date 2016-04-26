# -*- coding: utf-8 -*-

__all__ = (
    'Session',
)


class Session(object):
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.disable()

    def handle(self):
        pass

    def inject(self):
        pass

    enable = inject

    def disable(self):
        pass
