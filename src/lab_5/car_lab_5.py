"""Car Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Car Class
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

__title__ = "Car"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from automobile import Automobile


class Car(Automobile):
    """Car object."""

    __slots__ = ("__doors",)

    __doors: int

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        weight: int,
        acceleration: int,
        doors: int,
    ) -> None:
        """Initialize Car object."""
        super().__init__(make, model, year, weight, acceleration)
        self.set_doors(doors)

    def set_doors(self, doors: int) -> None:
        """Set doors."""
        self.__doors = doors

    def get_doors(self) -> int:
        """Get doors."""
        return self.__doors

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_doors()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tDoors: {self.get_doors()}"""
