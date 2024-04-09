#!/usr/bin/python3
"""Integer addition function defined."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    FBefore addition is performed, float arguments are typecated to ints

    Raises:
        TypeError: If either a or b is a non-integer non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
