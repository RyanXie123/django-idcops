# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# from distutils.core import setup
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_requirements():
    with open(os.path.join(
            os.path.dirname(__file__), "requirements.txt")) as f:
        requirements_list = [req.strip() for req in f.readlines()]
    return requirements_list


setup(
    name='idcops',
    version='2.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='A data center inventory management software',
    long_description=README,
    url='https://www.idcops.cn/',
    author='Vivian Cheung',
    author_email='wenvki@gmail.com',
    install_requires=get_requirements(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.x',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.5',
)
