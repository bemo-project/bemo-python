# -*- coding: utf-8 -*-

from io import open
from setuptools import setup, find_packages


setup(
    name='bemo',
    version='0.0.0',
    description='TBD',
    long_description=open('README.md', encoding='utf-8').read(),
    author='Nikita Grishko',
    author_email='gr1n@protonmail.com',
    url='https://github.com/bemo-project/bemo-python',
    download_url='TBD',
    license='MIT',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
        'example',
    )),
    install_requires=(),
    extras_require={},
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
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
