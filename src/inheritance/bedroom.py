"""Bedroom Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Bedroom Class
# Last modified 2024/02/20
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

__title__ = "Bedroom"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from room import Room


class Bedroom(Room):
    """Bedroom object."""

    __slots__ = ("__color",)

    __color: str

    def __init__(
        self,
        width: int,
        length: int,
        color: str,
    ) -> None:
        """Initialize Bedroom object."""
        super().__init__(width, length)
        self.set_color(color)

    def set_color(self, color: str) -> None:
        """Set color."""
        self.__color = color

    def get_color(self) -> str:
        """Get color."""
        return self.__color

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_color()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tcolor = {self.get_color()!r}"""
