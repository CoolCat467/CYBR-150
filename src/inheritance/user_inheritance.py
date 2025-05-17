"""User Class."""

# Programmed by CoolCat467

from __future__ import annotations

# User Class
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

__title__ = "User"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class User:
    """User object."""

    __slots__ = ("__first_name", "__last_name")

    __first_name: str
    __last_name: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
    ) -> None:
        """Initialize User object."""
        self.set_first_name(first_name)
        self.set_last_name(last_name)

    def set_first_name(self, first_name: str) -> None:
        """Set first_name."""
        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        """Set last_name."""
        self.__last_name = last_name

    def get_first_name(self) -> str:
        """Get first_name."""
        return self.__first_name

    def get_last_name(self) -> str:
        """Get last_name."""
        return self.__last_name

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_first_name()!r}, {self.get_last_name()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\tfirst_name = {self.get_first_name()!r}
\tlast_name = {self.get_last_name()!r}"""
