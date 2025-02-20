"""Automobile Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Automobile Class
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

__title__ = "Automobile"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Automobile:
    """Automobile object."""

    __slots__ = ("__acceleration", "__make", "__model", "__weight", "__year")

    __make: str
    __model: str
    __year: int
    __weight: int
    __acceleration: int

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        weight: int,
        acceleration: int,
    ) -> None:
        """Initialize Automobile object.

        Weight is in kilograms.
        Acceleration is in meters per second.
        """
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)
        self.set_weight(weight)
        self.set_acceleration(acceleration)

    def set_make(self, make: str) -> None:
        """Set make."""
        self.__make = make

    def set_model(self, model: str) -> None:
        """Set model."""
        self.__model = model

    def set_year(self, year: int) -> None:
        """Set year."""
        self.__year = year

    def set_weight(self, weight: int) -> None:
        """Set weight."""
        self.__weight = weight

    def set_acceleration(self, acceleration: int) -> None:
        """Set acceleration."""
        self.__acceleration = acceleration

    def get_make(self) -> str:
        """Get make."""
        return self.__make

    def get_model(self) -> str:
        """Get model."""
        return self.__model

    def get_year(self) -> int:
        """Get year."""
        return self.__year

    def get_weight(self) -> int:
        """Get weight."""
        return self.__weight

    def get_acceleration(self) -> int:
        """Get acceleration."""
        return self.__acceleration

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_make()!r}, {self.get_model()!r}, {self.get_year()!r}, {self.get_weight()!r}, {self.get_acceleration()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tMake: {self.get_make()}
\tModel: {self.get_model()}
\tYear: {self.get_year()}
\tWeight: {self.get_weight()} kg
\tAcceleration: {self.get_acceleration()} m/s"""
