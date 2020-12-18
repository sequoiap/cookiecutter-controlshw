# cookiecutter-controlshw

A cookiecutter template for all the Controls Homework problems by Sequoia
Ploeg.


## Getting Started

See the [tutorial](./tutorial/README.md) for setup and usage instructions.

To use the cookiecutter, assuming you already have cookiecutter installed, run

```
cookiecutter https://github.com/sequoiap/cookiecutter-controlshw
```

The resulting project can be installed by navigating to the directory
containing `setup.py` and running

```
pip install -e .
```

## Maintainers

The docstrings used throughout this cookiecutter adhere to the 
[NumPy docstring standard](https://numpydoc.readthedocs.io/en/latest/format.html). 
A couple callout items:

1. Docstring sections are in the same order as described by the numpydoc format.
2. Docstrings for ``__init__`` are in the  main class docstring (including 
parameters, warnings, examples) and not below the actual ``__init__`` function 
declaration.
