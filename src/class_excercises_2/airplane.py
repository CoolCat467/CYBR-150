"""Airplane Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Airplane Class
# Last modified 2024/02/16
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

__title__ = "Airplane"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Airplane:
    """Airplane object."""

    __slots__ = (
        "__brand",
        "__engine_number",
        "__model",
        "__passenger_number",
        "__top_speed",
    )

    __brand: str
    __model: str
    __engine_number: int
    __passenger_number: int
    __top_speed: float

    def __init__(
        self,
        brand: str,
        model: str,
        engine_number: int,
        passenger_number: int,
        top_speed: float,
    ) -> None:
        """Initialize Airplane object."""
        self.set_brand(brand)
        self.set_model(model)
        self.set_engine_number(engine_number)
        self.set_passenger_number(passenger_number)
        self.set_top_speed(top_speed)

    def time_to_arrive(self, distance: float) -> float:
        """Return time to travel given distance (in miles), measured in hours."""
        return distance / self.get_top_speed()

    def set_brand(self, brand: str) -> None:
        """Set brand."""
        self.__brand = brand

    def set_model(self, model: str) -> None:
        """Set model."""
        self.__model = model

    def set_engine_number(self, engine_number: int) -> None:
        """Set engine_number."""
        self.__engine_number = engine_number

    def set_passenger_number(self, passenger_number: int) -> None:
        """Set passenger_number."""
        self.__passenger_number = passenger_number

    def set_top_speed(self, top_speed: float) -> None:
        """Set top_speed."""
        self.__top_speed = top_speed

    def get_brand(self) -> str:
        """Get brand."""
        return self.__brand

    def get_model(self) -> str:
        """Get model."""
        return self.__model

    def get_engine_number(self) -> int:
        """Get engine_number."""
        return self.__engine_number

    def get_passenger_number(self) -> int:
        """Get passenger_number."""
        return self.__passenger_number

    def get_top_speed(self) -> float:
        """Get top_speed."""
        return self.__top_speed

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_brand()!r}, {self.get_model()!r}, {self.get_engine_number()!r}, {self.get_passenger_number()!r}, {self.get_top_speed()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tbrand = {self.get_brand()!r}
\tmodel = {self.get_model()!r}
\tengine_number = {self.get_engine_number()!r}
\tpassenger_number = {self.get_passenger_number()!r}
\ttop_speed = {self.get_top_speed()!r}"""

    def __lt__(self, rhs: object) -> bool:
        """Return if this Airplane's passenger_number is less than other Airplane's passenger_number, or NotImplemented if not a Airplane object."""
        if not isinstance(rhs, Airplane):
            return NotImplemented
        return self.get_passenger_number() < rhs.get_passenger_number()

    def __gt__(self, rhs: object) -> bool:
        """Return if this Airplane's passenger_number is greater than other Airplane's passenger_number, or NotImplemented if not a Airplane object."""
        if not isinstance(rhs, Airplane):
            return NotImplemented
        return self.get_passenger_number() > rhs.get_passenger_number()

    def __eq__(self, rhs: object) -> bool:
        """Return if this Airplane's passenger_number is equal to other Airplane's passenger_number, or NotImplemented if not a Airplane object."""
        if not isinstance(rhs, Airplane):
            return NotImplemented
        return self.get_passenger_number() == rhs.get_passenger_number()

    def equal_to(self, other: Airplane) -> bool:
        """Return if all attributes match."""
        return (
            self.get_brand() == other.get_brand()
            and self.get_model() == other.get_model()
            and self.get_engine_number() == other.get_engine_number()
            and self.get_passenger_number() == other.get_passenger_number()
            and self.get_top_speed() == other.get_top_speed()
        )

    def compare_to(self, other: Airplane) -> int:
        """Return -1 if other > self, 0 if other == self, and 1 if other < self.

        Raises ValueError if somehow none of the comparison branches match.
        """
        if self < other:
            return 1
        if self > other:
            return -1
        if self == other:
            return 0
        raise ValueError("Should be unreachable.")
