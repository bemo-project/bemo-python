# -*- coding: utf-8 -*-

import sys
from io import open
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(
    name='bemo',
    version='0.0.3.dev0',
    description='It\'s simple way to mock your back-end from webdriver UI tests',
    long_description=open('README.rst', encoding='utf-8').read(),
    author='Nikita Grishko',
    author_email='gr1n@protonmail.com',
    url='https://github.com/bemo-project/bemo-python',
    download_url='https://pypi.python.org/pypi/bemo/',
    license='MIT',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
        'example',
    )),
    install_requires=(
        'Jinja2==2.11.3',
    ),
    extras_require={
        'py2x': [
            'enum34',
            'httpstatus35',
        ],
    },
    tests_require=(
        'tox',
    ),
    cmdclass={
        'test': Tox,
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
