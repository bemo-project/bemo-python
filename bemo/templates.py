# -*- coding: utf-8 -*-

import json

from jinja2 import Environment, PackageLoader

__all__ = (
    'xhook__initialize',
    'xhook__enable',
    'xhook__disable',
)


# Initialize Jinja2 environment
_env = Environment(loader=PackageLoader('bemo', 'templates'))

# Initialize templates
_xhook__initialize = _env.get_template('xhook/initialize.jinja2')
_xhook__enable = _env.get_template('xhook/enable.jinja2')
_xhook__disable = _env.get_template('xhook/disable.jinja2')


# Define helpers for templates
def xhook__initialize(context):
    return render(_xhook__initialize, context=context)


def xhook__enable():
    return render(_xhook__enable)


def xhook__disable():
    return render(_xhook__disable)


def render(tmpl, context=None):
    context = context or {}

    return tmpl.render(bemo=json.dumps(context))
