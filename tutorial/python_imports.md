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

## Python's Import Path

Python's import path is a variable that stores a list of paths (directory
locations on your computer) where Python will look for installed packages. 
Since there can be multiple directories for it to look through, it goes through
them in order; if it doesn't find it in the first one, it looks at the second,
all the way until it's run out of places on its "path" variable.

The import system looks through the following locations (in this order) and 
stops looking after the first match:

1. The directory of the current script (or terminal directory).
1. The contents of its path variable (called `PYTHONPATH`).
1. Other installation-dependent directories.

So, if you have NumPy installed, it's downloaded to some place that your
environment knows about (some buried folder on your computer). But, if you're
working from a directory where you also created your own `numpy.py` file,
that'll be the first one found by the Python interpreter and it will obscure
the actual package.

So, don't name files with the same name as a package you'd like to use! But
where this is advantageous is, if you create a directory with several files,
it's very easy to import those files for use within each other. You can try 
out the following exercise, if you'd like:

1. Create a folder for our temporary experiment, perhaps named `deleteme`.
1. Create a Python file named `mymath.py` with the following contents:

    ```
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b
    ```

1. Create a Python file named `runner.py`. Try it any one version of the
   following, and note how they are all equivalent:

    The typical way of importing and using a library.

    ```
    import mymath

    a = 2
    b = 4

    c = mymath.add(a, b)
    d = mymath.subtract(a, b)
    e = mymath.multiply(a, b)
    f = mymath.divide(a, b)
    
    print(c, d, e, f)
    ```

    If the library name is super long, you can alias it to a shorthand version.
    NumPy, for example, is almost always imported as `np`. Any code examples
    you find online or on Stack Overflow will do this.

    ```
    import mymath as mm

    a = 2
    b = 4

    c = mm.add(a, b)
    d = mm.subtract(a, b)
    e = mm.multiply(a, b)
    f = mm.divide(a, b)

    print(c, d, e, f)
    ```

    You can also import everything from a file or package into your namespace
    using a wildcard import (`*`). Then you don't have to type the package name
    before each function call. This is considered bad practice, however, as it
    "pollutes" your namespace, often bringing in a lot of unknown functions and
    potentially overwriting ones you defined.

    ```
    from mymath import *
    
    a = 2
    b = 4

    c = add(a, b)
    d = subtract(a, b)
    e = multiply(a, b)
    f = divide(a, b)

    print(c, d, e, f)
    ```

    You can also alias specific functions as you import them.

    ```
    from mymath import add as A
    from mymath import subtract as S
    from mymath import multiply as M
    from mymath import divide as D

    a = 2
    b = 4

    c = A(a, b)
    d = S(a, b)
    e = M(a, b)
    f = D(a, b)

    print(c, d, e, f)
    ```

    You can delete your temporary folder now.

## Creating and Installing a Local Package

The homework repositories are set up as a software package. That means not only
is it a set of scripts, but they behave as a self-aware package. What this
means for you is that, as long as your files and scripts are within the main
package directory and the directory containing them has an `__init__.py` file,
they can be imported by any other script within your package. 

This is because, during setup, we ran `pip install -e .`. That means your
environment interpreter now knows where to find anything that begins with your
package name, regardless of what directory you are in on your computer.

For example, within the `project_name` directory there is a file called
`parameters.py`.

```
- project_name
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
import project_name.parameters as P
```

The line above "namespaces" or aliases everything within `parameters.py` to the
variable `P`. The values can then be accessed as `P.[attribute]` (e.g.,
`P.mass`).

**WARNING:** DO NOT REMOVE THE EMPTY ``__init__.py`` FILE! Imports won't work
otherwise. It's perfectly alright that they are empty files. This is just how
Python works.

## Creating a simulation without creating a installable package

So long as all the files are within a single folder, Python can find them all
pretty easily without having to be informed about paths. The homeworks are
created as an installable package as you use the same files for different
assignments, which are separated by folder. But for an exam, say, you might
want to create a simulation without having to create an installable Python
program; you just want all the files you need in a single folder.

Imagine the following folder structure, for example:

```
- project_name
  |-- animation.py
  |-- controller.py
  |-- dynamics.py
  |-- parameters.py
  |-- plotter.py
  \-- sim.py
```

Within the `sim.py` file, for example, you could have the following lines:

```
import parameters as P
from controller import Controller
from dynamics import Dynamics
```

Since they're all in the same directory, Python knows how to find them without
having to have a "package" installed and on its PATH variable.

---

Next Topic: [System Simulation: The structure of a simulation](simulation_structure.md)