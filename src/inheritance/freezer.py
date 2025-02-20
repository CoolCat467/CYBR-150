"""Freezer Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Freezer Class
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

__title__ = "Freezer"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from appliance import Appliance


class Freezer(Appliance):
    """Freezer object."""

    __slots__ = ("__low_temp",)

    __low_temp: int

    def __init__(
        self,
        type_: str,
        brand: str,
        low_temp: int,
    ) -> None:
        """Initialize Freezer object."""
        super().__init__(type_, brand)
        self.set_low_temp(low_temp)

    def set_low_temp(self, low_temp: int) -> None:
        """Set low_temp."""
        self.__low_temp = low_temp

    def get_low_temp(self) -> int:
        """Get low_temp."""
        return self.__low_temp

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_low_temp()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tlow_temp = {self.get_low_temp()!r}"""
