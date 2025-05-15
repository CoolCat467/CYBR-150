"""Staff Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Staff Class
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

__title__ = "Staff"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from user import User


class Staff(User):
    """Staff object."""

    __slots__ = ("__department", "__title")

    __department: str
    __title: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
        id_: int,
        department: str,
        title: str,
    ) -> None:
        """Initialize Staff object."""
        super().__init__(first_name, last_name, id_)
        self.set_department(department)
        self.set_title(title)

    def __eq__(self, other: object) -> bool:
        """Return if equal to other object."""
        if not isinstance(other, Staff):
            return False

        return (
            self.get_first_name() == other.get_first_name()
            and self.get_last_name() == other.get_last_name()
            and self.get_id() == other.get_id()
            and self.get_department() == other.get_department()
            and self.get_title() == other.get_title()
        )

    def equal_to(self, other: Staff) -> bool:
        """Return if equal to other Staff object."""
        return self == other

    def set_department(self, department: str) -> None:
        """Set department."""
        self.__department = department

    def set_title(self, title: str) -> None:
        """Set title."""
        self.__title = title

    def get_department(self) -> str:
        """Get department."""
        return self.__department

    # N815: Variable `get_Department` in class scope should not be mixedCase
    get_Department = get_department  # noqa: N815

    def get_title(self) -> str:
        """Get title."""
        return self.__title

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{super().__repr__()[:-1]}, {self.get_department()!r}, {self.get_title()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{super().__str__()}
\tdepartment = {self.get_department()!r}
\ttitle = {self.get_title()!r}"""
