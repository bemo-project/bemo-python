# -*- coding: utf-8 -*-

from selenium import webdriver
from selene import conditions, tools

import bemo


wd = webdriver.Firefox()
tools.set_driver(wd)

tools.visit('https://accounts.google.com/SignUp')

with bemo.Session(wd=wd) as session:
    session.handle('InputValidator', body={
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

    tools.s('#GmailAddress').set('John Snow')
    tools.s('#submitbutton').click()

    tools.s('#errormsg_0_GmailAddress').should_have(conditions.text('It work.'))
