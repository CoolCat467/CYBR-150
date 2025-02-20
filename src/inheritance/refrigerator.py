"""Refrigerator Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Refrigerator Class
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

__title__ = "Refrigerator"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from appliance import Appliance


class Refrigerator(Appliance):
    """Refrigerator object."""

    __slots__ = ("__volume",)

    __volume: int

    def __init__(
        self,
        type_: str,
        brand: str,
        volume: int,
    ) -> None:
        """Initialize Refrigerator object."""
        super().__init__(type_, brand)
        self.set_volume(volume)

    def set_volume(self, volume: int) -> None:
        """Set volume."""
        self.__volume = volume

    def get_volume(self) -> int:
        """Get volume."""
        return self.__volume

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_volume()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tvolume = {self.get_volume()!r}"""
