"""Polygon class."""

# Programmed by CoolCat467

from __future__ import annotations

# Polygon class
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

__title__ = "Polygon"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"


class Polygon:
    """Polygon class."""

    __slots__ = ("__name", "__sides")

    def __init__(self, name: str, sides: int) -> None:
        """Initialize polygon."""
        self.set_name(name)
        self.set_sides(sides)

    def __eq__(self, rhs: object) -> bool:
        """Return if self == rhs."""
        if not isinstance(rhs, Polygon):
            return NotImplemented
        return (
            self.get_name() == rhs.get_name()
            and self.get_sides() == rhs.get_sides()
        )

    def equal_to(self, other: Polygon) -> bool:
        """Return if this object is equivalent to other."""
        return self == other

    def get_name(self) -> str:
        """Return name."""
        return self.__name

    def get_sides(self) -> int:
        """Return side count."""
        return self.__sides

    def set_name(self, name: str) -> None:
        """Set name."""
        self.__name = name

    def set_sides(self, sides: int) -> None:
        """Set side count."""
        self.__sides = sides

    def __repr__(self) -> str:
        """Return representation of this object."""
        return f"{self.__class__.__name__}({self.get_name()!r}, {self.get_sides()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"{self.__class__.__name__}\n\tName = {self.get_name()}\n\tSides = {self.get_sides()!r}"
