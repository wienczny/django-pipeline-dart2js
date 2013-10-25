# -*- coding: utf-8 -*-
import os
from setuptools import setup

setup(
    name='django-pipeline-dart2js',
    version='0.1.0',
    description='django-pipeline compiler for dart2js.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Stephan Wienczny',
    author_email='wienczny@gmail.com',
    license = 'Apache License v2',
    url='https://github.com/wienczny/django-pipeline-dart2js',
    packages=['pipeline_dart2js'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Compilers',
    ]
)
