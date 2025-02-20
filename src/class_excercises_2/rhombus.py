"""Rhombus Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Rhombus Class
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

__title__ = "Rhombus"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Rhombus:
    """Rhombus object."""

    __slots__ = ("__diag_1", "__diag_2", "__side_length")

    __side_length: int
    __diag_1: int
    __diag_2: int

    def __init__(
        self,
        side_length: int,
        diag_1: int,
        diag_2: int,
    ) -> None:
        """Initialize Rhombus object."""
        self.set_side_length(side_length)
        self.set_diag_1(diag_1)
        self.set_diag_2(diag_2)

    def get_perimeter(self) -> int:
        """Return perimeter of this Rhombus."""
        return self.get_side_length() * 4

    def get_area(self) -> float:
        """Return the area of this Rhombus."""
        return (self.get_diag_1() * self.get_diag_2()) / 2

    def set_side_length(self, side_length: int) -> None:
        """Set side_length."""
        self.__side_length = side_length

    def set_diag_1(self, diag_1: int) -> None:
        """Set diag_1."""
        self.__diag_1 = diag_1

    def set_diag_2(self, diag_2: int) -> None:
        """Set diag_2."""
        self.__diag_2 = diag_2

    def get_side_length(self) -> int:
        """Get side_length."""
        return self.__side_length

    def get_diag_1(self) -> int:
        """Get diag_1."""
        return self.__diag_1

    def get_diag_2(self) -> int:
        """Get diag_2."""
        return self.__diag_2

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_side_length()!r}, {self.get_diag_1()!r}, {self.get_diag_2()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tside_length = {self.get_side_length()!r}
\tdiag_1 = {self.get_diag_1()!r}
\tdiag_2 = {self.get_diag_2()!r}"""

    def __lt__(self, rhs: object) -> bool:
        """Return if this rhombus's area is less than other rhombus's area, or NotImplemented if not a rhombus object."""
        if not isinstance(rhs, Rhombus):
            return NotImplemented
        return self.get_area() < rhs.get_area()

    def __gt__(self, rhs: object) -> bool:
        """Return if this rhombus's area is greater than other rhombus's area, or NotImplemented if not a rhombus object."""
        if not isinstance(rhs, Rhombus):
            return NotImplemented
        return self.get_area() > rhs.get_area()

    def __eq__(self, rhs: object) -> bool:
        """Return if this rhombus's area is equal to other rhombus's area, or NotImplemented if not a rhombus object."""
        if not isinstance(rhs, Rhombus):
            return NotImplemented
        return self.get_area() == rhs.get_area()

    def equal_to(self, other: Rhombus) -> bool:
        """Return if all attributes match."""
        return (
            self.get_side_length() == other.get_side_length()
            and self.get_diag_1() == other.get_diag_1()
            and self.get_diag_2() == other.get_diag_2()
        )

    def compare_to(self, other: Rhombus) -> int:
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
