# -*- coding: utf-8 -*-

from io import open
from setuptools import setup, find_packages


setup(
    name='bemo',
    version='0.0.0',
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
        'Jinja2==2.8',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
