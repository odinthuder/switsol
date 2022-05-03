# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip._internal.req import parse_requirements # changed pip.req to pip._internal.req
import re, ast


# get version from __version__ variable in switsol/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('switsol/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="false")	

setup(
	name='switsol',
	version=version,
	description='Switsol',
	author='Switsol',
	author_email='jitendra.k@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.requirement) for ir in requirements], # changed to str(ir.req) to str(ir.requirement)
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)



#!/usr/bin/env python3
# Path: setup.py
