# {{cookiecutter.project_name}}

## Getting started

Make sure your conda environment is activated. Then, after navigating into
the directory containing this file (the toplevel of your brand new Python
package) in a conda terminal (using `cd`), you can simply run `make build`.

## Running Simulations from the Toplevel

You can either run simulations by navigating to the appropriate folder and
running, in a terminal (after activating your environment):

```
python sim.py
```

Alternatively, you can run them from the package toplevel with the command:

```
python {{cookiecutter.project_name}} -hw 12 -p
```

Program command line arguments can be seen by running:

```
python {{cookiecutter.project_name}} -h
```

## "Packaging" for the novice Python programmer

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

## Words of caution

### Numpy arrays

Make sure that when you create column vectors that you use double brackets. 

Consider the following:

```
>>> a = np.array([[5], [3]]) # This is a column vector
>>> b = np.array([5, 3]) # This is not; this is a row vector

>>> a.shape
(2,1)
>>> b.shape
(2,)
>>> b.T.shape # Even the transpose of a (2,) array is (2,), not (1,2)!
(2,)

>>> c = np.array([[5, 3]]) # This is a more specific row vector than even `b`
>>> c.shape
(1, 2)
>>> c.T.shape # Now transposing has an effect.
(2, 1)
```

It's very common to lose track of what's a numpy array already and just keep
wrapping arrays in numpy arrays, making the dimensions larger and larger and
leading to problems down the road. Make sure to keep track of what's an array
and what's not, and when you multiply by a value and store it in an array,
even if the value is only a (1,1) numpy array, extract the value so you just
have an integer before performing operations with it.