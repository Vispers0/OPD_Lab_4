import math
from math import pi


def cube(side, precision):
    if type(side) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for side must be integers or floats, arguments for precision are integers")

    if side < 0 or precision < 0:
        raise ValueError("Cube side cant be negative")

    sq = round(side ** 3, precision)
    return sq


def prism(base_sq, height, precision):
    if (type(base_sq) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if base_sq < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round(base_sq * height, precision)
    return sq


def parallel(base_sq, height, precision):
    if (type(base_sq) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if base_sq < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round(base_sq * height, precision)
    return sq


def rect_parallel(length, width, height, precision):
    if (type(length) or type(width) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if length < 0 or width < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round(length * width * height, precision)
    return sq


def pyramid(base_sq, height, precision):
    if (type(base_sq) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if base_sq < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round((1/3) * base_sq * height, precision)
    return sq


def tetra(side, precision):
    if type(side) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if side < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round((side ** 3 * math.sqrt(2)) / 12, precision)
    return sq


def cylinder(rad, height, precision):
    if (type(rad) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if rad < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round(pi * rad ** 2 * height, precision)
    return sq


def cone(rad, height, precision):
    if (type(rad) or type(height)) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if rad < 0 or height < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round((1/3) * pi * rad ** 2 * height, precision)
    return sq


def ball(rad, precision):
    if type(rad) not in [int, float] or type(precision) not in [int]:
        raise TypeError("Arguments for the figure must be integers or floats, arguments for precision are integers")

    if rad < 0 or precision < 0:
        raise ValueError("One of the values is negative")

    sq = round((4/3) * pi * rad ** 3, precision)
    return sq
