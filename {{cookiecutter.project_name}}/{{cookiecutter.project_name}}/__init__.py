"""
{{cookiecutter.project_name}}

A simulator for control problems.
"""

import platform
import sys

if sys.version_info < (3, 0, 0):
    raise Exception(
        "{{cookiecutter.project_name}} requires Python 3 (version "
        + platform.python_version()
        + " detected)."
    )
