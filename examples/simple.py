# -*- coding: utf-8 -*-

from selenium import webdriver
from selene.conditions import text
from selene.tools import set_driver, visit, s

import bemo


wd = webdriver.Firefox()
set_driver(wd)

visit('https://accounts.google.com/SignUp')

with bemo.Session(wd=wd) as session:
    handler = session.handle('InputValidator', body={
        'input01': {
            'Valid': 'false',
            'ErrorMessage': 'Error!',
            'Errors': {
                'GmailAddress': 'It work.',
            },
            'ErrorData': [],
        },
        'Locale': 'ru',
    })
    session.inject()

    s('#GmailAddress').set('John Snow')
    s('#submitbutton').click()

    s('#errormsg_0_GmailAddress').should_have(text('It work.'))

    handler.assert_called_once_with({
        'method': 'POST',
        'url': 'InputValidator?resource=SignUp',
    })
