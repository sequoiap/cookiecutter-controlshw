[Home](README.md)

Previous Topic: [Environment Setup: Using Anaconda and Visual Studio Code](environment_setup.md)

# Third Party Packages: NumPy, SciPy, Matplotlib, and Control libraries

In the languages beginning students are most familiar with (C++, Java, or C),
there is the concept of libraries that provide functions you can call. For
example, in C++ you can do the following:

```
#include <cmath>
```

This allows you to access functions such as `sqrt()`, `round()`, and `log()`.
The main idea is, when you start a random new file in some language, unless you
start writing a bunch of functions yourself, you're going to very limited in
what you can do. Now, consider what we'd like to do in this class: create
simulations of various complex systems, visualize them and their performance
(that means graphing and animating), do lots of math to compute control inputs
(think about how you'd calculate sines, cosines, and multiply matrices if you
had to implement those from scratch), etc. Would you like to write the code
that creates plots on a screen? Nope! This is where third party libraries come
in real handy. Other people have already implemented these libraries for you,
and given you the ability to download (for free!) their packages and use their
code in your own code. They even provide a helpful Application Programming
Interface (API)--this is the set functions you'd call within their library,
with specific arguments or parameters, to get the desired return values--that
is (usually) well documented on a website.

Let's talk about the most useful third-party packages you'll be using. To 
follow along with the examples, open up your terminal/Anaconda Prompt, activate
your environment, and type `python` to open up the interactive interpreter.

## NumPy and SciPy

Documentation: [NumPy](https://numpy.org/doc/stable/), [SciPy](https://docs.scipy.org/doc/scipy/reference/)

NumPy is a matrix/multi-dimensional mathematics library for Python. It was
actually created by BYU Alumnus Travis Oliphant. Many of its functions are
similarly named to MATLAB, and it can basically do most of the things MATLAB
can do, but with Python syntax. Many scientists and engineers favor Python with
NumPy and SciPy over MATLAB, however, because it's open-source and free (MATLAB
is VERY expensive).

Below are some of it's more useful features for us. In the examples that
follow, note that is conventional to `import numpy as np` for easier use of the
library.

### Arrays and Matrices

You can create arrays, or better called conceptualized as "vectors," by passing
Python lists as an argument to `np.array()`.

```
import numpy as np

a = [1, 2, 3, 4, 5]
a_vector = np.array(a)
# Equivalently,
a_vector = np.array([1, 2, 3, 4, 5])
```

Numpy arrays have **dimensions**. When you simply pass a list, it creates a 
one-by-*undefined* array.

```
a_vector.shape
# Returns (5,)
```

If you want something defined specifically as a row or column vector, you must
add more square brackets to force the shape.

```
# This creates a row vector; one row, five columns.
a = np.array([[1, 2, 3, 4, 5]])

# This creates a column vector; five columns, one row.
a = np.array([[1],
              [2],
              [3],
              [4],
              [5]])

# This also creates a column vector; whitespace doesn't really change things in
# a programming language
a = np.array([[1], [2], [3], [4], [5]])

# This also creates a column vector by using NumPy's transpose attribute.
a = np.array([[1, 2, 3, 4, 5]]).T
```

### Matrix Multiplication

Most NumPy multiplication of arrays is element-wise. If you want matrix
multiplication, you should use the `@` operator.

```
# Element-wise multiplication
a = np.array([[1, 2, 3]])
b = np.array([[2, 4, 6]])
c = a * b
c
# returns: array([[ 2, 8, 18]])

# Matrix multiplicatoin
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[1, 1]]).T    # Transpose because matrices multiply by column vectors
c = a @ b
c
# returns: array([[3], [7]])
```

### Dimensional words of Caution
Make sure that when you create column vectors that you use double brackets. 

Try the following:

```
>>> import numpy as np
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
leading to problems down the road. For example,

```
>>> import numpy as np
>>> a = np.array([1, 2, 3])
>>> a
array([1, 2, 3])

>>> b = np.array([a])
>>> b
array([[1, 2, 3]])
# Note, we gained a dimension!

>>> c = np.array([c])
>>> c
array([[[1, 2, 3]]])
```

Make sure to keep track of what's an array and what's not, and when you
multiply by a value and store it in an array, even if the value is only a (1,1)
numpy array, extract the value (perhaps using `var.item(0)`) so you just have
an integer before performing operations with it. Example:

```
>>> import numpy as np
>>> a = np.array([1])
>>> b = a.item(0)
>>> b
1
# Note, it's not an array! Just a number.

>>> c = np.array([b])
# Now c is back to a (1,1) array. Good!
```

## Matplotlib

Documentation: [Matplotlib](https://matplotlib.org/)

Matplotlib functions very similar to MATLAB. For example:

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x,y)
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

## Control

Documentation: [Control](https://python-control.readthedocs.io/en/latest/)

You'll learn a lot more about this library later in the course. But, it
provides many of the functions that implemented in MATLAB for control systems
design that aren't part of a general purpose numerical package like NumPy. 

---

Next Topic: [Python Packages: Imports explained](python_imports.md)