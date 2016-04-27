# -*- coding: utf-8 -*-

from selenium import webdriver
from selene import tools

import bemo


wd = webdriver.Firefox()
tools.set_driver(wd)

tools.visit('https://accounts.google.com/SignUp')

with bemo.Session(wd=wd) as session:
    session.inject()
