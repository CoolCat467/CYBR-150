"""Rectangle class."""

# Programmed by CoolCat467

from __future__ import annotations

# Rectangle class
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

__title__ = "Rectangle"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"


from polygon import Polygon


class Rectangle(Polygon):
    """Rectangle class."""

    __slots__ = ("__height", "__width")

    def __init__(self, name: str, sides: int, width: int, height: int) -> None:
        """Initialize Rectangle."""
        super().__init__(name, sides)
        self.set_width(width)
        self.set_height(height)

    def get_area(self) -> int:
        """Return area of this Rectangle."""
        return self.get_width() * self.get_height()

    def get_perimeter(self) -> int:
        """Return the perimeter of this Rectangle."""
        width = self.get_width()
        height = self.get_height()
        return (width + height) * 2

    def __eq__(self, rhs: object) -> bool:
        """Return if self == rhs."""
        if not isinstance(rhs, Rectangle):
            return NotImplemented
        return (
            super().__eq__(rhs)
            and self.get_width() == rhs.get_width()
            and self.get_height() == rhs.get_height()
        )

    def equal_to(self, other: Polygon) -> bool:
        """Return if this object is equivalent to other."""
        return self == other

    def get_width(self) -> int:
        """Return width."""
        return self.__width

    def get_height(self) -> int:
        """Return side count."""
        return self.__height

    def set_width(self, width: int) -> None:
        """Set width."""
        self.__width = width

    def set_height(self, height: int) -> None:
        """Set side count."""
        self.__height = height

    def __repr__(self) -> str:
        """Return representation of this object."""
        previous = super().__repr__()[:-1]
        return f"{previous}, {self.get_width()!r}, {self.get_height()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"{super().__str__()}\n\tWidth = {round(self.get_width(), 2)}\n\tHeight = {round(self.get_height(), 2)}\n\tArea = {self.get_area()}\n\tPerimeter = {self.get_perimeter()}"
