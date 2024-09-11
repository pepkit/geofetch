#! /usr/bin/env python

import os
import sys

from setuptools import setup

PACKAGE = "geofetch"
REQDIR = "requirements"

# Additional keyword arguments for setup().
extra = {}

# Ordinary dependencies


def read_reqs(reqs_name):
    deps = []
    with open(os.path.join(REQDIR, "requirements-{}.txt".format(reqs_name)), "r") as f:
        for line in f:
            if not line.strip():
                continue
            # deps.append(line.split("=")[0].rstrip("<>"))
            deps.append(line)
    return deps


DEPENDENCIES = read_reqs("all")
extra["install_requires"] = DEPENDENCIES

scripts = None

with open("{}/_version.py".format(PACKAGE), "r") as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")

with open("README.md") as f:
    long_description = f.read()

setup(
    name=PACKAGE,
    packages=[PACKAGE],
    version=version,
    description="Downloads data and metadata from GEO and SRA and creates standard PEPs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="project, bioinformatics, sequencing, ngs, workflow, GUI",
    url="https://github.com/pepkit/{}/".format(PACKAGE),
    author="Oleksandr Khoroshevskyi, Nathan Sheffield, Vince Reuter, Nathan LeRoy",
    license="BSD2",
    entry_points={
        "console_scripts": [
            "geofetch = geofetch.__main__:main",
            "sraconvert = geofetch.sraconvert:main",
        ],
    },
    package_data={PACKAGE: ["templates/*"]},
    scripts=scripts,
    include_package_data=True,
    test_suite="tests",
    tests_require=read_reqs("dev"),
    setup_requires=(
        ["pytest-runner"] if {"test", "pytest", "ptr"} & set(sys.argv) else []
    ),
    **extra,
)
