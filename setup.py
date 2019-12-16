# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('jsearch/jsearch.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-jsearch",
    packages = ["jsearch"],
    entry_points = {
        "console_scripts": ['jsearch = jsearch.jsearch:main']
        },
    version = version,
    description = "Python command line application jsearch",
    long_description = long_descr,
    author = "Ishtiaq Ahmed",
    author_email = "ishtiaq.1982@gmail.com",
    url = "https://github.com/techish1/jsearch.git",
    )
