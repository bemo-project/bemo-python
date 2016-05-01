# -*- coding: utf-8 -*-

import json

from bemo import handlers, templates


def test_render_all_templates():
    """
    Stupid test for checking that all template successfully rendered.
    """
    assert templates.xhook__initialize({})
    assert templates.xhook__handlers({})
    assert templates.xhook__enable()
    assert templates.xhook__release()
    assert templates.asserts__call_count({})
    assert templates.asserts__calls({})


def test_json_encoder():
    handler = handlers.Handler('urlpart', body={
        'key': 'value',
    })

    assert json.dumps(handler, cls=templates.JSONEncoder) == json.dumps({
        'uid': handler.uid,
        'urlpart': handler.urlpart,
        'status': handler.status.value,
        'statusText': handler.status.name,
        'headers': handler.headers,
        'body': handler.body,
    })
