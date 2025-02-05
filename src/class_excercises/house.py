"""House Class."""

# Programmed by CoolCat467

from __future__ import annotations

# House Class
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

__title__ = "House"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class House:
    """House object."""

    __slots__ = (
        "__current_price",
        "__num_bathrooms",
        "__num_rooms",
        "__total_square_foot",
    )

    __num_rooms: int
    __num_bathrooms: int
    __total_square_foot: int
    __current_price: float

    def __init__(
        self,
        num_rooms: int,
        num_bathrooms: int,
        total_square_foot: int,
        current_price: float,
    ) -> None:
        """Initialize House object."""
        self.set_num_rooms(num_rooms)
        self.set_num_bathrooms(num_bathrooms)
        self.set_total_square_foot(total_square_foot)
        self.set_current_price(current_price)

    def set_num_rooms(self, num_rooms: int) -> None:
        """Set num_rooms."""
        self.__num_rooms = num_rooms

    def set_num_bathrooms(self, num_bathrooms: int) -> None:
        """Set num_bathrooms."""
        self.__num_bathrooms = num_bathrooms

    def set_total_square_foot(self, total_square_foot: int) -> None:
        """Set total_square_foot."""
        self.__total_square_foot = total_square_foot

    def set_current_price(self, current_price: float) -> None:
        """Set current_price."""
        self.__current_price = current_price

    def get_num_rooms(self) -> int:
        """Get num_rooms."""
        return self.__num_rooms

    def get_num_bathrooms(self) -> int:
        """Get num_bathrooms."""
        return self.__num_bathrooms

    def get_total_square_foot(self) -> int:
        """Get total_square_foot."""
        return self.__total_square_foot

    def get_current_price(self) -> float:
        """Get current_price."""
        return self.__current_price

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_num_rooms()!r}, {self.get_num_bathrooms()!r}, {self.get_total_square_foot()!r}, {self.get_current_price()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tnum_rooms = {self.get_num_rooms()!r}
\tnum_bathrooms = {self.get_num_bathrooms()!r}
\ttotal_square_foot = {self.get_total_square_foot()!r}
\tcurrent_price = {self.get_current_price()!r}"""
