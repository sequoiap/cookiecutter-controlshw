# -*- coding: utf-8 -*-
#
# Copyright © Control Book Project Contributors
# Licensed under the terms of the MIT License
# (see {{cookiecutter.project_name}}/__init__.py for details)

"""
Installation (setup.py) for {{cookiecutter.project_name}}
"""

import sys

import setuptools

# ==============================================================================
# Constants
# ==============================================================================
NAME = "{{cookiecutter.project_name}}"
LIBNAME = "{{cookiecutter.project_name}}"

# ==============================================================================
# Setup arguments
# ==============================================================================
setup_args = dict(
    name=NAME,
    author="{{cookiecutter.author}}",
    platforms=["Windows", "Linux", "Mac OS-X"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
)

install_requires = [
    "scipy>=1.2.1",
    "numpy",
    "pytest",
]

if "setuptools" in sys.modules:
    setup_args["install_requires"] = install_requires


# ==============================================================================
# Main setup
# ==============================================================================
setuptools.setup(**setup_args)