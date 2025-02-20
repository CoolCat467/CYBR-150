"""Truck Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Truck Class
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

__title__ = "Truck"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from automobile import Automobile


class Truck(Automobile):
    """Truck object."""

    __slots__ = ("__drive_type",)

    __drive_type: int

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        weight: int,
        acceleration: int,
        drive_type: int,
    ) -> None:
        """Initialize Truck object."""
        super().__init__(make, model, year, weight, acceleration)
        self.set_drive_type(drive_type)

    def set_drive_type(self, drive_type: int) -> None:
        """Set drive_type."""
        self.__drive_type = drive_type

    def get_drive_type(self) -> int:
        """Get drive_type."""
        return self.__drive_type

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_drive_type()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tDrive Type: {self.get_drive_type()}"""
