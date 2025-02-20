"""My_Circle Class."""

# Programmed by CoolCat467

from __future__ import annotations

# My_Circle Class
# Last modified 2024/02/13
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

__title__ = "My_Circle"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


import math


# N801 - Class name `My_Circle` should use CapWords convention
class My_Circle:  # noqa: N801
    """My_Circle object."""

    __slots__ = ("__name", "__radius")

    __radius: int
    __name: str

    def __init__(self, name: str, radius: int) -> None:
        """Initialize My_Circle object."""
        self.set_name(name)
        self.set_radius(radius)

    def get_area(self) -> float:
        """Return the area of this circle."""
        radius = self.get_radius()
        return math.pi * radius * radius

    def get_diameter(self) -> int:
        """Return the diameter of this circle."""
        return self.get_radius() * 2

    def get_circumference(self) -> float:
        """Return the circumference of this circle."""
        return math.pi * self.get_diameter()

    def set_name(self, name: str) -> None:
        """Set name."""
        self.__name = name

    def set_radius(self, radius: int) -> None:
        """Set radius."""
        self.__radius = radius

    def get_name(self) -> str:
        """Get name."""
        return self.__name

    def get_radius(self) -> int:
        """Get radius."""
        return self.__radius

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_name()!r}, {self.get_radius()})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tname = {self.get_name()}
\tradius = {self.get_radius()}
\tarea = {self.get_area():.02f}
\tdiameter = {self.get_diameter()}
\tcircumference = {self.get_circumference():.02f}"""

    def __lt__(self, other: object) -> bool:
        """Return < comparison of radius."""
        if not isinstance(other, My_Circle):
            return NotImplemented
        return self.get_radius() < other.get_radius()

    def __gt__(self, other: object) -> bool:
        """Return > comparison of radius."""
        if not isinstance(other, My_Circle):
            return NotImplemented
        return self.get_radius() > other.get_radius()

    def __eq__(self, other: object) -> bool:
        """Return == comparison of radius."""
        if not isinstance(other, My_Circle):
            return NotImplemented
        return self.get_radius() == other.get_radius()

    def compare_to(self, other: object) -> int:
        """Return comparison integer of this circle and another object.

        -2 if not a My_Circle instance or nonmatching comparison.
        -1 if this circle radius < other circle radius.
        0 if this circle radius == other circle radius.
        1 if this circle radius > other circle radius.
        """
        if not isinstance(other, My_Circle):
            return -2
        if self < other:
            return -1
        if self > other:
            return 1
        if self == other:
            return 0
        return -2

    def equal_to(self, other: My_Circle) -> bool:
        """Return if this circle's name and radius are equal to other object."""
        return self == other and self.get_name() == other.get_name()
