[Home](README.md)

Previous Topic: [About Python](about_python.md)

# Environment Setup: Using Anaconda and Visual Studio Code

## What's an environment?

In the development world, it's pretty typical for a single developer to be 
working on several programs or pieces of software at the same time (though not
simultaneously!). With that many in-development programs on the same computer,
it's generally considered good practice to keep their respective environments
"separate" and "clean", isolated from each other. 

For example, suppose we're working on two projects, but they each depend on a
different release version of some third party library. Well, we can't just
download that library to our computer and make it globally available--it's
presence will "infect" the workspace of the other, rendering that project
unusable. So what to do?

We use "environments." In Python, they're generally referred to as "virtual
environments," something that can be activated or deactivated as necessary
(say, within a terminal or code editor/IDE)and that contains all the
third-party libraries or variables needed by one specific project, thereby not
changing any system-wide settings or affecting other projects on the computer.

The rest of this page walks you through setting up a virtual environment on
your machine.

## What's Anaconda? (And why Windows is the absolute worst.)

Many operating systems come with Python preinstalled (MacOS and Linux do, but
not Windows). Some operating systems are therefore easier to set up for
development. Still, there are many people in the world who use an operating
system that doesn't come with Python (looking at you, Windows). Unfortunately,
the default Python version that can be installed on said operating system isn't
as user-friendly as it is on other machines (you can't directly enter the
Python interpreter from the default terminal without some extensive setup).

Anaconda is a data-science focused Python distribution that also has some neat
features like package management, virtual environments, and overall makes the
MacOS and Linux development workflow available on an unnamed operating system
(*cough cough* Windows). With Anaconda, you can access Python in a terminal,
install packages using `pip`, create as many virtual environments as your heart
desires with whatever version of Python your heart desires, and so is what I
recommend for using Python on Windows (and Mac). 

For Linux, well--if you're using Linux, I presume you are smart enough (and
likely opinionated enough) to know how you prefer to setup development
environments. You can use Anaconda on Linux, but I know I prefer just using the
default Python. I'll leave that up to you, though.

## Setting up your computer

1. Install Anaconda

    You can get the free, open-source [Anaconda Individual
    Edition](https://www.anaconda.com/products/individual). If you're on
    Windows, it's best to not already have Python installed; I'm not sure how
    well conflicting versions behave together. (Note that if you're on Linux,
    it will add a line to your `.bashrc` that will make Anaconda Python the
    default in the terminal, obscuring your system Python. It's probably the
    same on a Mac.)

1. Install Visual Studio Code (VSCode) or some other IDE

    My recommendation is to install, as your text editor,
    [VSCode](https://code.visualstudio.com/) \(although you can easily do it
    with something like [PyCharm](https://www.jetbrains.com/pycharm/) or
    [Atom](https://atom.io/)--but all my instructions will be for VSCode\). I
    personally think PyCharm does too much, has too many configuration settings
    that mess people up, and in general makes beginner programmers *worse*
    programmers because they don't understand what's going on under-the-hood.
    
    Visual Studio Code is different from Visual Studio (looking at you, "I used
    Visual Studio in my CS class" people). It's far more lightweight; it's just
    a code editor (so, a much nicer looking Notepad++) with a lot of extensions
    available to make developing much nicer (like Python autocompletion and
    Intellisense). It's open-source but backed by Microsoft, and it's
    cross-platform (so you can use it on Windows, Mac, or Linux).

1. Create the virtual environment

    Now we need to create the virtual environment you'll do all your
    development in for this class. There are three projects, but they all use
    the same dependencies, so we can use the same environment across all three
    projects (so long as you name your three project folders uniquely! That
    goes without saying).

    Open:
    * Windows: Anaconda Prompt (search in start menu)
    * Mac: I don't own a Mac, I assume you'll just open a terminal
    * Linux: Terminal (remember, these instructions are for using Anaconda)

    The following command will create a new environment:

    ```
    conda create -n <you-pick-a-reasonable-name> python
    ```

    I would recommend a short, all-lowercase, no-symbol, no-spaces name (e.g.,
    `controls`). After that's been created, activate it in the terminal with
    the following command:

    ```
    conda activate <the-environment-name-you-chose>
    ```

    Note you'll have to activate your environment every time you start Anaconda 
    Prompt in order to access your installed Python packages.

1. Create a directory for your homework projects

    Choose where you want all your homework files to be stored this semester.
    I recommend creating a single folder in, say, your `Documents` folder that
    will be home to all three simulations' project directories. That's what 
    I'll assume you've done going forward: 
    
    ```
    Documents/controls>
    ```

1. Get the cookiecutter

    Install the cookiecutter package to Anaconda by using this command in the 
    Anaconda Prompt (or terminal)--make sure your environment is activated!

    ```
    conda install -c conda-forge cookiecutter
    ```

    After navigating to your `controls` directory in the terminal (using `cd`,
    google how to use the "cd command"), you can create a new directory based
    off the controls cookiecutter by using the command:

    ```
    cookiecutter <url-to-repo>
    ```

    As your directory is created, respond to the prompts; they will autofill
    values throughout the project template. Suggested project names would be
    `mass`, `ballbeam`, and `vtol`. (When I say suggested, I really mean you
    should use those.)

1. Install your homework packages

    Python will run your simulations using other files within your project. It
    needs to therefore know how to find them. While Python's import system will
    be described later in the tutorial, suffice it to say you need to install
    the packages we just created to your environment. You can do this by
    navigating into each homework project's toplevel directory (so, *into*
    `mass`, `ballbeam`, and `vtol`) and running:

    ```
    pip install -e .
    ```

    Short explanation: `pip install` installs to your active environment the
    package that follows in the command line arguments; `-e` is a flag that
    means "editable," meaning if the code changes in the source library, those
    changes reflected in the installed version; `.` means current directory,
    which is the package to install, if you're terminal is in the right place.

1. Set up the debugger

    Now, open up VSCode. VSCode has the nice feature of opening up entire
    folders and displaying the directory in a sidepane for easy access to the
    whole project directory.

    

    If your newly created environment isn't showing up in VSCode, you can go
    to the terminal and, after activating your environment, running the command

    ```
    which python
    ```

    This should yield (on the first line of perhaps a few) the path to your
    environment's python interpreter. You can always copy this path and
    manually add it to VSCode (when you click on the interpreter button, select
    "Enter interpreter path...")

---

Next Topic: [Third Party Packages: NumPy, SciPy, Matplotlib, and Control libraries](third_party_packages.md)