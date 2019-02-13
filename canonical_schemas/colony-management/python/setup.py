#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='colony_management_pipeline',
    version='0.0.0',
    description='Datajoint schemas for mouse colony management, adopted from IBL project',
    author='Vathes',
    author_email='support@vathes.com',
    packages=find_packages(exclude=[]),
    install_requires=['datajoint'],
    scripts=['scripts/colony-management-shell.py'],
)
