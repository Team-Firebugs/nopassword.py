# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

with open('LICENSE') as f:
    license = f.read()

requirements = []
with open("requirements.txt") as f:
    requirements = [x.split("=")[0].strip() for x in f.readlines()]

setup(
    name='nopassword',
    version='0.0.4',
    description='Determenistic password generator',
    long_description=read_md('README.md'),
    #long_description=readme,
    author='oskarnyqvist',
    author_email='oskarnyqvist@gmail.com',
    url='https://github.com/nopassword/nopass.py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires= requirements,
    scripts=['bin/nopassword'],
    )
