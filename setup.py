# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in neokred_api/__init__.py
from neokred_api import __version__ as version

setup(
	name='neokred_api',
	version=version,
	description='card api',
	author='openetech',
	author_email='hello@openetech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
