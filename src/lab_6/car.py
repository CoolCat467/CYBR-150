"""Car Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Car Class
# Last modified 2024/02/24
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


class Car:
    """Car object."""

    __slots__ = (
        "__acceleration",
        "__cur_speed",
        "__deceleration",
        "__dist",
        "__max_speed",
        "__owner",
        "__speeds",
        "__trip_time",
    )

    __owner: str
    __cur_speed: int
    __dist: int
    __trip_time: float
    __max_speed: int
    __speeds: list[int]
    __acceleration: int
    __deceleration: int

    def __init__(
        self,
        owner: str,
        cur_speed: int = 0,
        dist: int = 0,
        trip_time: float = 0.0,
        max_speed: int = 100,
        acceleration: int = 5,
        deceleration: int = 5,
    ) -> None:
        """Initialize Car object."""
        self.set_max_speed(max_speed)
        self.set_speeds([])

        self.set_owner(owner)
        self.set_cur_speed(cur_speed)
        self.set_dist(dist)
        self.set_trip_time(trip_time)

        self.set_acceleration(acceleration)
        self.set_deceleration(deceleration)

    def set_owner(self, owner: str) -> None:
        """Set owner."""
        self.__owner = owner

    def set_cur_speed(self, cur_speed: int) -> None:
        """Set cur_speed."""
        self.__cur_speed = min(self.get_max_speed(), cur_speed)
        self.__speeds.append(self.__cur_speed)

    def set_dist(self, dist: int) -> None:
        """Set dist."""
        self.__dist = dist

    def set_trip_time(self, trip_time: float) -> None:
        """Set trip_time."""
        self.__trip_time = trip_time

    def set_max_speed(self, max_speed: int) -> None:
        """Set max_speed."""
        self.__max_speed = max_speed

    def set_speeds(self, speeds: list[int]) -> None:
        """Set speeds."""
        self.__speeds = speeds

    def set_acceleration(self, acceleration: int) -> None:
        """Set acceleration."""
        self.__acceleration = acceleration

    def set_deceleration(self, deceleration: int) -> None:
        """Set deceleration."""
        self.__deceleration = deceleration

    def get_owner(self) -> str:
        """Get owner."""
        return self.__owner

    def get_cur_speed(self) -> int:
        """Get cur_speed."""
        return self.__cur_speed

    def get_dist(self) -> int:
        """Get dist."""
        return self.__dist

    def get_trip_time(self) -> float:
        """Get trip_time."""
        return self.__trip_time

    def get_max_speed(self) -> int:
        """Get max_speed."""
        return self.__max_speed

    def get_acceleration(self) -> int:
        """Get acceleration."""
        return self.__acceleration

    def get_deceleration(self) -> int:
        """Get deceleration."""
        return self.__deceleration

    def get_speeds(self) -> list[int]:
        """Get speeds."""
        return self.__speeds

    def accelerate(self, iteration: int) -> None:
        """Set current speed to acceleration times iteration."""
        self.set_cur_speed(self.get_acceleration() * iteration)

    def brake(self) -> None:
        """Set current speed to the current speed minus deceleration."""
        self.set_cur_speed(self.get_cur_speed() - self.get_deceleration())

    def get_avg_speed(self) -> float:
        """Return average of speeds."""
        speeds = self.get_speeds()
        return sum(speeds) / len(speeds)

    def move(self) -> None:
        """Move one unit and update trip time."""
        self.set_dist(self.get_dist() + 1)
        # "Set the trip time to the current trip time plus 60 divided by
        # the current speed"
        # is dubious, does it mean
        # (current trip time + 60) / current speed
        # or
        # current trip time + (60 / current speed)
        #
        # self.set_trip_time((self.get_trip_time() + 60) / self.get_cur_speed())
        self.set_trip_time(self.get_trip_time() + (60 / self.get_cur_speed()))

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_owner()!r}, {self.get_cur_speed()!r}, {self.get_dist()!r}, {self.get_trip_time()!r}, {self.get_max_speed()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tOwner:\t\t{self.get_owner()}
\tCurrent Speed:\t{self.get_cur_speed()} Mph
\tDistance:\t{self.get_dist()} Miles
\tTime:\t\t{self.get_trip_time():.03f} Minutes
\tMax Speed:\t{self.get_max_speed()} Mph
\tAverage Speed:\t{self.get_avg_speed()} Mph"""
