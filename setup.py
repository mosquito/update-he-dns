# encoding: utf-8

from __future__ import absolute_import, print_function

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.1'
__author__ = 'Dmitry Orlov <me@mosquito.su>'


setup(name='update-he-dns',
      version=__version__,
      author=__author__,
      author_email='me@mosquito.su',
      license="MIT",
      description="Simple DYNDNS updater for dns.he.net",
      platforms="all",
      url="http://github.com/mosquito/update-he-dns",
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python',
      ],
      long_description=open('README.rst').read(),
      scripts=['bin/update-he-dns', ],
      requires=['Python (>2.6)']
      )
