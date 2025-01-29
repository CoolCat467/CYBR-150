"""CYBR 150 - Exercise I."""

# Programmed by CoolCat467

from __future__ import annotations

# CYBR 150 - Exercise I
# Copyright (C) 2025  CoolCat467
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__title__ = "Exercise I"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"

import sys

assert sys.version_info >= (3, 12), "Using type parameter syntax, new in 3.12."

##Exercise 1:
##
##Make a function that manually creates a 10x10 two-dimensional array
##filled with X's. Use an integer variable to determine the size and a
##val variable to determine the content.


def ten_x_2d_manual() -> list[list[str]]:
    """Return 10x10 2d array of 'X's."""
    # Confused by "manual" here, implies return constant array, but
    # with size instruction, that's not possible.
    size = 10
    # Could store before return, but why bother? (also linter removes)
    return [["X"] * size for _ in range(size)]


##Exercise 2:
##
##Make a function that creates a two-dimensional array just like Ex 1
##using the naive approach.


def ten_x_2d_naive() -> list[list[str]]:
    """Return 10x10 2d array of 'X's."""
    size = 10
    val: list[list[str]] = []
    for _ in range(size):
        row: list[str] = []
        for _ in range(size):
            row.append("X")
        val.append(row)
    return val


##Exercise 3:
##
##Make a function that creates a three-dimensional array just like Ex 1
##using the naive approach.


def ten_x_3d_naive() -> list[list[list[str]]]:
    """Return 10x10x10 3d array of 'X's."""
    size = 10
    x: list[list[list[str]]] = []
    for _ in range(size):
        y: list[list[str]] = []
        for _ in range(size):
            z: list[str] = []
            for _ in range(size):
                z.append("X")
            y.append(z)
        x.append(y)
    return x


##Exercise 4:
##
##Make a function that creates a two-dimensional array just like Ex 1
##using the naive approach. Fill with the string "Nothing"


def ten_nothing_2d_naive() -> list[list[str]]:
    """Return 10x10 2d array of 'Nothing'."""
    size = 10
    val: list[list[str]] = []
    for _ in range(size):
        row: list[str] = []
        for _ in range(size):
            row.append("Nothing")
        val.append(row)
    return val


##Exercise 5:
##
##Make a function that creates a three-dimensional array just like Ex 1
##using the naive approach. Fill with the integer 1.


def ten_1_3d_naive() -> list[list[list[int]]]:
    """Return 10x10x10 3d array of 1s."""
    size = 10
    x: list[list[list[int]]] = []
    for _ in range(size):
        y: list[list[int]] = []
        for _ in range(size):
            z: list[int] = []
            for _ in range(size):
                z.append(1)
            y.append(z)
        x.append(y)
    return x


##Exercise 6:
##
##Make a function that creates a two-dimensional array like Ex 2 using
##Comprehensions.


def ten_x_2d() -> list[list[str]]:
    """Return 10x10 2d array of 'X's."""
    size = 10
    return [["X"] * size for _ in range(size)]


##Exercise 7:
##
##Make a function that creates a two-dimensional array like Ex 2 using
##Comprehensions. Fill with the string "Comps!".


def ten_comps_2d() -> list[list[str]]:
    """Return 10x10 2d array of 'Comps!'s."""
    size = 10
    return [["Comps!"] * size for _ in range(size)]


##Exercise 8:
##
##Write a function that takes in a size and a value, then creates a 2D
##array using comps just like above. Call it with the size of 20 and a
##value of “GO!”


def make_2d_array[T](size: int, value: T) -> list[list[T]]:
    """Return size x size 2d array of value."""
    return [[value] * size for _ in range(size)]


##Exercise 9:
##
##Write a function that takes in a size and a value, then creates a 3D
##array using comps just like above. Call it with a size of 5 and a
##value of 3.14.


def make_3d_array[T](size: int, value: T) -> list[list[list[T]]]:
    """Return size x size x size 3d array of value."""
    return [make_2d_array(size, value) for _ in range(size)]


##Exercise 10:
##
##Write a function that takes in a size and a value, then creates a 4D
##array using comps just like above. Call it with a size of 4 and a
##value of 0.


def make_4d_array[T](size: int, value: T) -> list[list[list[list[T]]]]:
    """Return size x size x size x size 4d array of value."""
    return [make_3d_array(size, value) for _ in range(size)]


def main() -> None:
    """Run program."""
    # 1
    print(f"{ten_x_2d_manual() = }")
    # 2
    print(f"{ten_x_2d_naive() = }")
    # 3
    print(f"{ten_x_3d_naive() = }")
    # 4
    print(f"{ten_nothing_2d_naive() = }")
    # 5
    print(f"{ten_1_3d_naive() = }")
    # 6
    print(f"{ten_x_2d() = }")
    # 7
    print(f"{ten_comps_2d() = }")
    # 8
    print(f"{make_2d_array(20, 'GO!') = }")
    # 9
    print(f"{make_3d_array(5, 3.14) = }")
    # 10
    print(f"{make_4d_array(4, 0) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
