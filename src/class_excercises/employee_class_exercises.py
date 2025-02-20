"""Employee Class."""

# Programmed by CoolCat467

from __future__ import annotations

# Employee Class
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

__title__ = "Employee"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


class Employee:
    """Employee object."""

    __slots__ = ("__email", "__employee_id", "__first_name", "__last_name")

    __employee_id: str
    __first_name: str
    __last_name: str
    __email: str

    def __init__(
        self,
        employee_id: str,
        first_name: str,
        last_name: str,
        email: str,
    ) -> None:
        """Initialize Employee object."""
        self.set_employee_id(employee_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

    def set_employee_id(self, employee_id: str) -> None:
        """Set employee_id."""
        self.__employee_id = employee_id

    def set_first_name(self, first_name: str) -> None:
        """Set first_name."""
        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        """Set last_name."""
        self.__last_name = last_name

    def set_email(self, email: str) -> None:
        """Set email."""
        self.__email = email

    def get_employee_id(self) -> str:
        """Get employee_id."""
        return self.__employee_id

    def get_first_name(self) -> str:
        """Get first_name."""
        return self.__first_name

    def get_last_name(self) -> str:
        """Get last_name."""
        return self.__last_name

    def get_email(self) -> str:
        """Get email."""
        return self.__email

    def __repr__(self) -> str:
        """Return representation of this object for python console."""
        return f"{self.__class__.__name__}({self.get_employee_id()!r}, {self.get_first_name()!r}, {self.get_last_name()!r}, {self.get_email()!r})"

    def __str__(self) -> str:
        """Return string representation of this object."""
        return f"""{self.__class__.__name__}:
\temployee_id = {self.get_employee_id()!r}
\tfirst_name = {self.get_first_name()!r}
\tlast_name = {self.get_last_name()!r}
\temail = {self.get_email()!r}"""
