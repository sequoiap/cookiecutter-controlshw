[Home](README.md)

Previous Topic: [Third Party Packages: NumPy, SciPy, Matplotlib, and Control libraries](third_party_packages.md)

# Python Packages: Imports 

A detailed explanation of the Python import system can be found [here](https://realpython.com/python-import/).

How does one access other Python files or functions? It seems that third party
packages just seem to mysteriously work. With one weird command `pip install
{x}` a whole library seems to be magically available at the wave of a hand
(well, that hand has to be waving over a keyboard and hitting the words `import
{x}` as it waves). But what about files *not* part of a third party library?
What if I want to use files that *I've* written in a different Python file?

## Definitions

* Modules
* Packages

## Absolute vs. Relative Imports

## Python's Import Path

## Creating and Installing a Local Package

This repository is set up as a software package. That means not only is it
a set of scripts, but they behave as a self-aware package. What this means
for you is that, as long as your files and scripts are within the main
package directory (in this case, `{{cookiecutter.project_name}}`) and the
directory containing them has an `__init__.py` file, they can be imported
by any other script within your package. 

For example, within the `{{cookiecutter.project_name}}` directory there is 
a file called `parameters.py`.

```
- {{cookiecutter.project_name}}
  |-- hw1/
  |-- hw2/
  |-- ...
  |-- hw[n]/
  |-- utils/
  |-- __init__.py
  |-- __main__.py
  \-- parameters.py
```

This file and its contained values can be used in any other python script
within the project by using the line

```
import {{cookiecutter.project_name}}.parameters as P
```

This namespaces everything within `parameters.py` to the variable `P`. The 
values can then be accessed as `P.[attribute]` (e.g., `P.mass`).

WARNING: DO NOT REMOVE THE ``__init__.py`` FILE! Imports won't work otherwise. 
It's perfectly alright that they are empty files. This is just how Python works.

---

Next Topic: [System Simulation: The structure of a simulation](simulation_structure.md)