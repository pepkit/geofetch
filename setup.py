#! /usr/bin/env python

import os
from setuptools import setup
import sys

PACKAGE = "geofetch"
REQDIR = "requirements"

# Additional keyword arguments for setup().
extra = {}


def read_reqs(reqs_name):
    deps = []
    with open(os.path.join(REQDIR, "requirements-{}.txt".format(reqs_name)), 'r') as f:
        for l in f:
            if not l.strip():
                continue
            #deps.append(l.split("=")[0].rstrip("<>"))
            deps.append(l)
    return deps


# 2to3
if sys.version_info >= (3, ):
    extra["use_2to3"] = True
extra["install_requires"] = read_reqs("all")


# Additional files to include with package
def get_static(name, condition=None):
    static = [os.path.join(name, f) for f in os.listdir(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), name))]
    if condition is None:
        return static
    else:
        return [i for i in filter(lambda x: eval(condition), static)]


# scripts to be added to the $PATH
# scripts = get_static("scripts", condition="'.' in x")
scripts = None

with open("{}/_version.py".format(PACKAGE), 'r') as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")

# Handle the pypi README formatting.
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError, OSError, RuntimeError):
    long_description = open('README.md').read()

setup(
    name=PACKAGE,
    packages=[PACKAGE],
    version=version,
    description="A ",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords="project, bioinformatics, sequencing, ngs, workflow, GUI",
    url="https://github.com/pepkit/{}/".format(PACKAGE),
    author=u"Nathan Sheffield, Vince Reuter",
    license="BSD2",
    entry_points={
        "console_scripts": [
            "{p} = {p}.{p}:main".format(p=PACKAGE)
        ],
    },
    package_data={PACKAGE: ['templates/*']},
    scripts=scripts,
    include_package_data=True,
    test_suite="tests", 
    tests_require=read_reqs("dev"),
    setup_requires=(["pytest-runner"] if {"test", "pytest", "ptr"} & set(sys.argv) else []), 
    **extra
)
