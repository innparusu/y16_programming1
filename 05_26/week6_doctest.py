"""This is "week6_doctest" module.

This module supplies one function, add(). For example,

>>> add(1, 2)
3

Note:
    If you want to do testing by doctest,
    type "python3 week6_doctest.py -v".

"""

def add(arg1, arg2):
    """Return the added value for arg1 and arg2.

    Args:
        arg1 (int or float): a number of int- or float-object.
        arg2 (int or float): a number of int- or float-object.

    Returns:
        int or float: the added value arg1 and arg2
    
    >>> add(-1, 3)
    2
    >>> add(0, 0.5)
    0.5
    """
    return arg1 + arg2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
