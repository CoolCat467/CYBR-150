"""Garage Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Garage Class
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

__title__ = "Garage"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from room import Room


class Garage(Room):
    """Garage object."""

    __slots__ = ("__bay_numbers",)

    __bay_numbers: int

    def __init__(
        self,
        width: int,
        length: int,
        bay_numbers: int,
    ) -> None:
        """Initialize Garage object."""
        super().__init__(width, length)
        self.set_bay_numbers(bay_numbers)

    def set_bay_numbers(self, bay_numbers: int) -> None:
        """Set bay_numbers."""
        self.__bay_numbers = bay_numbers

    def get_bay_numbers(self) -> int:
        """Get bay_numbers."""
        return self.__bay_numbers

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_bay_numbers()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tbay_numbers = {self.get_bay_numbers()!r}"""
