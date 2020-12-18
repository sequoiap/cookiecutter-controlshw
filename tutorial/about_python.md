[Home](README.md)

# About Python

What is Python? Python is an interpreted, high-level, general-purpose
programming language:

* **Interpreted** means that instructions (a.k.a. code) execute directly and
    freely without the need to be previously compiled into machine-language
    instructions. An interpreter executes your program directly.
* **High-level** means that many of the hardware-specific things about
    computers are strongly abstracted. For example, C is now generally
    considered a low-level language, as you have to manage memory yourself. In
    Python, this is not the case.
* **General-purpose** means that the language finds its way into many
    applications. For example, scientific computing is one of the most common
    use cases of Python these days. However, a significant portion of the web
    and modern servers or web content management systems are also powered by
    Python.

Python can often look like pseudocode--it's crazy how simple and easy some
things are to read in Python! Consider the following (working) examples:

```
# File operations
for line in open('filename'): 
    print(line )

# If/else statements
if "you" not in "love":
    print("sad")
else:
    print("Sequoia, what is going on here")
```

## Dynamically typed

If you're familiar with statically typed languages (like C, C++, etc.), you'll
be used to seeing variable definitions similar to

```
int a = 3;
```

Python, however, is dynamically typed, meaning you don't have to explicitly
state the type of the variable--it's inferred at assignment!

```
a = 3
```

There can be a danger to this, if you're not careful. Suppose you have a
variable, and you accidentally change it's type somewhere along the way by
reassigning something to it that you shouldn't have.

```
def add(a, b):
    """
    Adds two numbers together.
    """
    return a + b

c = 1
d = 2

c = Car() 
# Note that Python won't complain that you just completely changed the type
# of a variable! It'll happily believe that you, the programmer, know exactly
# what you're doing--often a dangerous assumption when you're a novice 
# programmer.

add(c, d)
# Python won't know how to add a Car to 2, and so will throw a RuntimeException.
```

I guess my point is, always know yourself what you expect a variable's type to
be and be careful where that variable might get used in the future if you
assign something else to it! Because Python won't stop you the way C might, 
it'll just keep chugging along, happy to turn an integer into a Car and try
adding it to another integer.

## Scripts vs. Interactive Shell

Since Python is interpreted, it can be run as a script or used in "interactive"
mode in a terminal, similar to MATLAB; MATLAB has scripts as well as the 
console window. 

Running a Python script is as simple as typing the command

```
python <filename.py>
```

This runs the file. Entering the interactive shell is as simple as typing

```
python
```

which brings opens the Python interpreter in the terminal. Once in the
interpreter, you can directly type python code, such as

```
a = 2
b = 3
c = a + b
print(c)
```

Once you've installed Python in the next step of the tutorial, try entering
interactive mode and typing out a few commands.

## Comments

You may be used to `//` comments in C/C++ or `%` in MATLAB. 

In Python, single line comments are denoted with `#`.

```
# This line is commented out
a = 3   # You can also comment out the rest of a line

# You could do multiline comments by adding a bunch of
# "hashtags" to each line of a paragraph.
```

Or, multiline comment blocks are denoted with three single- or
double-quotations.

```
'''
This section will be commented out
entirely.

Even this part!
'''

"""
Quotation marks work too!

Cool.
"""
```

Note that in most text editors, you can toggle comments for a selection by
hitting `ctrl + /`. Just highlight all the lines you want to comment out.

## Community

Python has a very large, very dedicated open-source community, especially in
the "scientific computing" domain. At the time of writing, there were nearly
280,000 packages available for download (free!) on the Python Package Index
([PyPI](https://pypi.org/)), a server where anyone can contribute packages or
libraries for doing all sorts of tasks. In fact, we'll download several third
party libraries from PyPI shortly. But, if you're interested, you can peruse
or search through the packages on PyPI to see what people out in "the wild" 
have written and uploaded for your convenience!

---

Next Topic: [Environment Setup: Using Anaconda and Visual Studio Code](environment_setup.md)