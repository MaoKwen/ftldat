#!/usr/bin/env python

from setuptools import setup, find_packages
import os, os.path

setup(name='ftldat3',
      version_config=True,
      setup_requires=['setuptools-git-versioning'],
      description='CLI tool to pack and unpack FTL .dat files',
      author='Bas Westerbaan',
      author_email='bas@westerbaan.name',
      url='http://github.com/bwesterb/ftldat/',
      packages=['ftldat'],
      package_dir={'ftldat': 'src'},
      install_requires = [''],
      entry_points = {
          'console_scripts': [
              'ftldat = ftldat.main:main',
              ]
          }
      )

# vim: et:sta:bs=2:sw=4:
