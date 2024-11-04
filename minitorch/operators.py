"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, List


#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def neg(a):
    return -a


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    return a if a >= b else b


def is_close(a, b):
    return abs(a - b) < 1e-2


def sigmoid(x):
    # \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))


def relu(x):
    return max(0.0, x)


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def inv(x):
    return 1.0 / x


def log_back(a, b):
    return b / a


def inv_back(a, b):
    return -b / (a**2)


def relu_back(a, b):
    return b if a > 0.0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(func: Callable, container: Iterable):
    for item in container:
        yield func(item)


def zipWith(func: Callable, container1: Iterable, container2: Iterable):
    for item1, item2 in zip(container1, container2):
        yield func(item1, item2)


def reduce(func: Callable, container: Iterable):
    el_cntr = 0
    ret_val = 0
    for item in container:
        el_cntr += 1
        if el_cntr == 1:
            ret_val = item
        else:
            ret_val = func(ret_val, item)

    return ret_val


def negList(container: List) -> List:
    return list(map(neg, container))


def addLists(container1: List, container2: List) -> List:
    return list(zipWith(add, container1, container2))


def sum(container: List):
    return reduce(add, container)


def prod(container: List):
    return reduce(mul, container)
