#!/usr/bin/env python3
from setuptools import setup

setup(name='joaoantonio',
      version='0.1',
      packages=['dev_aberto'],
      author='Joao Antonio',
      platforms=['any'],
      install_requires = ['requests'],
      scripts=['scripts/hello.py'],
      classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12']
      ),
