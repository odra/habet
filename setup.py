# -*- coding: utf-8 -*-
from setuptools import setup


options = {
  'name': 'habet',
  'version': '0.1',
  'description': 'python http framework on top of gevent (pywsgi)',
  'url': 'https://github.com/odra/habet',
  'author': 'Leonardo Rossetti',
  'author_email': 'leonardo@goldark.com.br',
  'license': 'MIT',
  'packages': ['habet'],
  'install_requires': [
    'routes',
    'gevent'
  ],
  'zip_safe': False  
}

setup(**options)
