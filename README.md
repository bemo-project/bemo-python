# bemo [![Requirements Status](https://requires.io/github/bemo-project/bemo-python/requirements.svg?branch=master)](https://requires.io/github/bemo-project/bemo-python/requirements/?branch=master) [![Build Status](https://travis-ci.org/bemo-project/bemo-python.svg?branch=master)](https://travis-ci.org/bemo-project/bemo-python)

Bemo(back-end mock) - it's simple way to mock your back-end from webdriver UI tests.

## Installation

Install `bemo` using [pip](http://www.pip-installer.org/):

    $ pip install bemo

...or install `bemo` running command below if use want to use Python 2.7:

    $ pip install bemo[py2x]

Enjoy!

## Usage

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

## Testing

Just run `tox` to test package.

## License

*bemo* is licensed under the MIT license. See the license file for details.

