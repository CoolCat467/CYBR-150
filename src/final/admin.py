"""Admin Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Admin Class
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


from user import User


class Admin(User):
    """Admin object."""

    __slots__ = ("__office_number", "__privilege_level")

    __privilege_level: int
    __office_number: int

    def __init__(
        self,
        first_name: str,
        last_name: str,
        id_: int,
        privilege_level: int,
        office_number: int,
    ) -> None:
        """Initialize Admin object."""
        super().__init__(first_name, last_name, id_)
        self.set_privilege_level(privilege_level)
        self.set_office_number(office_number)

    def __eq__(self, other: object) -> bool:
        """Return if equal to other object."""
        if not isinstance(other, Admin):
            return False

        return (
            self.get_first_name() == other.get_first_name()
            and self.get_last_name() == other.get_last_name()
            and self.get_id() == other.get_id()
            and self.get_privilege_level() == other.get_privilege_level()
            and self.get_office_number() == other.get_office_number()
        )

    def equal_to(self, other: Admin) -> bool:
        """Return if equal to other Admin object."""
        return self == other

    def compare_to(self, other: Admin) -> int:
        """Return 1 if privilege of self is higher than incoming, 0 if same, -1 if less."""
        if self.get_privilege_level() > other.get_privilege_level():
            return 1
        if self.get_privilege_level() < other.get_privilege_level():
            return -1
        return 0

    def set_privilege_level(self, privilege_level: int) -> None:
        """Set privilege_level."""
        self.__privilege_level = privilege_level

    def set_office_number(self, office_number: int) -> None:
        """Set office_number."""
        self.__office_number = office_number

    def get_privilege_level(self) -> int:
        """Get privilege_level."""
        return self.__privilege_level

    def get_office_number(self) -> int:
        """Get office_number."""
        return self.__office_number

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_privilege_level()!r}, {self.get_office_number()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tprivilage_level = {self.get_privilege_level()!r}
\toffice_number = {self.get_office_number()!r}"""
