"""Admin Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Admin Class
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

__title__ = "Admin"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from employee import Employee


class Admin(Employee):
    """Admin object."""

    __slots__ = ("__security_level",)

    __security_level: int

    def __init__(
        self,
        first_name: str,
        last_name: str,
        position_title: str,
        security_level: int,
    ) -> None:
        """Initialize Admin object."""
        super().__init__(first_name, last_name, position_title)
        self.set_security_level(security_level)

    def set_security_level(self, security_level: int) -> None:
        """Set security_level."""
        self.__security_level = security_level

    def get_security_level(self) -> int:
        """Get security_level."""
        return self.__security_level

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_security_level()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tsecurity_level = {self.get_security_level()!r}"""
