def func(arg):
    """TestCase for fun
    >>> func(1)
    1
    """
    print(arg)


def square(x):
    """
    Squares a number and returns the results.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Python2.6之后，可以直接在命令行运行testmod()：“python -m doctest -v test_func.py”；
