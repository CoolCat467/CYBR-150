"""Circle Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Circle Class
# Last modified 2024/02/16
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

__title__ = "Circle"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from math import pi


class Circle:
    """Circle object."""

    __slots__ = ("__radius",)

    __radius: int

    def __init__(self, radius: int) -> None:
        """Initialize Circle object."""
        self.set_radius(radius)

    def get_area(self) -> float:
        """Return the area of this circle."""
        r = self.get_radius()
        return pi * r * r

    def set_radius(self, radius: int) -> None:
        """Set radius."""
        self.__radius = radius

    def get_radius(self) -> int:
        """Get radius."""
        return self.__radius

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_radius()})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"{self.__class__.__name__}:\n\tradius = {self.get_radius()}"

    def __lt__(self, rhs: object) -> bool:
        """Return if this circle's radius is less than other circle's radius, or NotImplemented if not a Circle object."""
        if not isinstance(rhs, Circle):
            return NotImplemented
        return self.get_radius() < rhs.get_radius()

    def __gt__(self, rhs: object) -> bool:
        """Return if this circle's radius is greater than other circle's radius, or NotImplemented if not a Circle object."""
        if not isinstance(rhs, Circle):
            return NotImplemented
        return self.get_radius() > rhs.get_radius()

    def __eq__(self, rhs: object) -> bool:
        """Return if this circle's radius is equal to other circle's radius, or NotImplemented if not a Circle object."""
        if not isinstance(rhs, Circle):
            return NotImplemented
        return self.get_radius() == rhs.get_radius()

    equal_to = __eq__

    def compare_to(self, other: Circle) -> int:
        """Return -1 if other > self, 0 if other == self, and 1 if other < self.

        Raises ValueError if somehow none of the comparison branches match.
        """
        if self < other:
            return 1
        if self > other:
            return -1
        if self == other:
            return 0
        raise ValueError("Should be unreachable.")
