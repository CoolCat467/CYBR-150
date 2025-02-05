"""My_Circle Class."""

# Programmed by CoolCat467

from __future__ import annotations

# My_Circle Class
# Last modified 2024/02/04
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
        return f"{self.__class__.__name__}:\n\tname = {self.get_name()}\n\tradius = {self.get_radius()}"
