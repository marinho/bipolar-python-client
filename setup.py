#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from bipolar.version import version_number

setup(
    name='bipolar-client',
    version=version_number,
    description='Bipolar client',
    long_description='''Bipolar client.''',
    keywords='python bipolar feature toggle switch',
    author='Marinho Brandao',
    author_email='marinho@gmail.com',
    url='http://github.com/marinho/bipolar-client/',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
    ],
)
