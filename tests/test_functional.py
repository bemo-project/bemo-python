# -*- coding: utf-8 -*-

from collections import OrderedDict

from bemo import functional


def test_partial_match():
    original = {
        'method': 'POST',
        'url': '/some/url/to',
        'key': 'value',
    }
    expected = {
        'method': 'POST',
    }
    assert functional.partial_match(original, expected)

    original = {
        'method': 'POST',
        'url': '/some/url/to',
    }
    expected = {
        'method': 'POST',
        'key': 'value',
    }
    assert not functional.partial_match(original, expected)


def test_deep_sort():
    expected = OrderedDict([
        ('asdaq1mma', '11oakka'),
        ('eejjjajjaii', '28uj2wghq'),
        ('n1hhauii1j', OrderedDict([
            ('ckakkjqja', OrderedDict([
                ('2jj199jj2hjh1', '2nnhh22a'),
                ('sjj2jhh1', '2288hjbdbbak'),
            ])),
            ('wkjj1ii8', '123111akk'),
        ])),
    ])
    original = {
        'asdaq1mma': '11oakka',
        'n1hhauii1j': {
            'wkjj1ii8': '123111akk',
            'ckakkjqja': {
                '2jj199jj2hjh1': '2nnhh22a',
                'sjj2jhh1': '2288hjbdbbak',
            },
        },
        'eejjjajjaii': '28uj2wghq',
    }
    assert functional.deep_sort(original) == expected
