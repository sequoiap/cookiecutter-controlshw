# cookiecutter-controlshw
A cookiecutter template for all the Controls Homework problems by Sequoia Ploeg.


# Getting Started

We'll use Anaconda for our Python environments. You can download it [here](). 
If you know how to use Python environments already, feel free to create your
own whichever way you want. If you've done Python development and don't want to
switch to Anaconda Python (which will override existing Python installations, at
least in Linux), just create a virtual Python environment some other way.

Within the Anaconda Prompt (to run in Windows, search "Anaconda Prompt" in the 
start menu), we'll create a new environment using the command:

```
conda create -n <you-pick-a-reasonable-name> python
```

I would recommend a short, all-lowercase, no-symbol name (e.g., `controls`). 
After that's been created, activate it with the command shown in the terminal:

```
conda activate <the-environment-name-you-chose>
```

Note you'll have to activate your environment every time you start Anaconda 
Prompt in order to access your installed Python packages.

Install the following packages by using these commands in the prompt:

```
conda install -c conda-forge cookiecutter
<!-- conda install -c anaconda make -->
```

You can create a new directory based off this cookiecutter by using the command:

```
cookiecutter url-to-repo
```

As your directory is created, respond to the prompts to autofill values 
throughout the project. Suggested project names would be `mass`, `ballbeam`, 
and `vtol`. (When I say suggested, I really mean you should use those.)

# Maintainers

The docstrings used throughout this cookiecutter adhere to the 
[NumPy docstring standard](https://numpydoc.readthedocs.io/en/latest/format.html). 
A couple callout items:

1. Docstring sections are in the same order as described by the numpydoc format.
2. Docstrings for ``__init__`` are in the  main class docstring (including 
parameters, warnings, examples) and not below the actual ``__init__`` function 
declaration.
