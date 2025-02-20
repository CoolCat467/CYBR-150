"""Appliance Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Appliance Class
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

__title__ = "Appliance"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Appliance:
    """Appliance object."""

    __slots__ = ("__brand", "__type")

    __type: str
    __brand: str

    def __init__(
        self,
        type_: str,
        brand: str,
    ) -> None:
        """Initialize Appliance object."""
        self.set_type(type_)
        self.set_brand(brand)

    def set_type(self, type_: str) -> None:
        """Set type."""
        self.__type = type_

    def set_brand(self, brand: str) -> None:
        """Set brand."""
        self.__brand = brand

    def get_type(self) -> str:
        """Get type."""
        return self.__type

    def get_brand(self) -> str:
        """Get brand."""
        return self.__brand

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_type()!r}, {self.get_brand()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\ttype = {self.get_type()!r}
\tbrand = {self.get_brand()!r}"""
