# -*- coding: utf-8 -*-

import json

from jinja2 import Environment, PackageLoader

from bemo import handlers

__all__ = (
    'xhook__initialize',
    'xhook__handlers',
    'xhook__enable',
    'xhook__release',

    'asserts__call_count',
)


# Initialize Jinja2 environment
_env = Environment(loader=PackageLoader('bemo', 'templates'))

# Initialize templates
_xhook__initialize = _env.get_template('xhook/initialize.jinja2')
_xhook__handlers = _env.get_template('xhook/handlers.jinja2')
_xhook__enable = _env.get_template('xhook/enable.jinja2')
_xhook__release = _env.get_template('xhook/release.jinja2')
_asserts__call_count = _env.get_template('asserts/call_count.jinja2')


# Define helpers for templates
def xhook__initialize(context):
    return render(_xhook__initialize, context=context)


def xhook__handlers(context):
    return render(_xhook__handlers, context=context)


def xhook__enable():
    return render(_xhook__enable)


def xhook__release():
    return render(_xhook__release)


def asserts__call_count(context):
    return render(_asserts__call_count, context=context)


# Render templates helpers
class JSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode `bemo` handlers.
    """
    def default(self, o):
        if isinstance(o, handlers.Handler):
            return {
                'uid': o.uid,
                'urlpart': o.urlpart,
                'status': o.status.value,
                'statusText': o.status.name,
                'headers': o.headers,
                'body': o.body,
            }

        return super(JSONEncoder, self).default(o)


def render(tmpl, context=None):
    context = context or {}
    context = json.dumps(context, cls=JSONEncoder)

    return tmpl.render(bemo=context)
