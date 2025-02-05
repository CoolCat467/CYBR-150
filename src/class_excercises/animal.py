"""Animal Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Animal Class
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

__title__ = "Animal"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Animal:
    """Animal object."""

    __slots__ = ("__legs", "__name", "__size", "__type")

    __type: str
    __legs: int
    __size: int
    __name: str

    def __init__(
        self,
        type_: str,
        legs: int,
        size: int,
        name: str,
    ) -> None:
        """Initialize Animal object."""
        self.set_type(type_)
        self.set_legs(legs)
        self.set_size(size)
        self.set_name(name)

    def set_type(self, type_: str) -> None:
        """Set type."""
        self.__type = type_

    def set_legs(self, legs: int) -> None:
        """Set legs."""
        self.__legs = legs

    def set_size(self, size: int) -> None:
        """Set size."""
        self.__size = size

    def set_name(self, name: str) -> None:
        """Set name."""
        self.__name = name

    def get_type(self) -> str:
        """Get type."""
        return self.__type

    def get_legs(self) -> int:
        """Get legs."""
        return self.__legs

    def get_size(self) -> int:
        """Get size."""
        return self.__size

    def get_name(self) -> str:
        """Get name."""
        return self.__name

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_type()!r}, {self.get_legs()!r}, {self.get_size()!r}, {self.get_name()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\ttype = {self.get_type()!r}
\tlegs = {self.get_legs()!r}
\tsize = {self.get_size()!r}
\tname = {self.get_name()!r}"""
