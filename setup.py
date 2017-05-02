#!/usr/bin/python

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='colorprint',  # This is the name of your PyPI-package.
    version='1.0.1',      # Update the version number for new releases
    description='Color print function for Python',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/GH0st3rs/colorprint',
    author='GH0st3rs',
    author_email='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Natural Language :: Russian',
        'Natural Language :: English',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
