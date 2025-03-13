"""Triangle Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Triangle Class
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

__title__ = "Triangle"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Triangle:
    """Triangle object."""

    __slots__ = ("__height", "__length")

    __height: int
    __length: int

    def __init__(self, height: int, length: int) -> None:
        """Initialize triangle object."""
        self.set_height(height)
        self.set_length(length)

    def set_height(self, height: int) -> None:
        """Set height."""
        self.__height = height

    def set_length(self, length: int) -> None:
        """Set length."""
        self.__length = length

    def get_height(self) -> int:
        """Get height."""
        return self.__height

    def get_length(self) -> int:
        """Get length."""
        return self.__length

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_height()}, {self.get_length()})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"{self.__class__.__name__}:\n\tHeight = {self.get_height()}\n\tLength = {self.get_length()}"
