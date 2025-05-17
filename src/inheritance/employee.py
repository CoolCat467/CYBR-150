"""Employee Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Employee Class
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

__title__ = "Employee"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from user_inheritance import User


class Employee(User):
    """Employee object."""

    __slots__ = ("__position_title",)

    __position_title: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
        position_title: str,
    ) -> None:
        """Initialize Employee object."""
        super().__init__(first_name, last_name)
        self.set_position_title(position_title)

    def set_position_title(self, position_title: str) -> None:
        """Set position_title."""
        self.__position_title = position_title

    def get_position_title(self) -> str:
        """Get position_title."""
        return self.__position_title

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_position_title()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tposition_title = {self.get_position_title()!r}"""
