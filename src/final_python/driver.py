"""Driver - Test class functionality."""

# Programmed by CoolCat467

from __future__ import annotations

# Driver - Test class functionality
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

__title__ = "Driver"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from admin import Admin
from staff import Staff


def main() -> None:
    """Run program."""
    john = Admin("John", "Von Neumann", 29, 5, 301)
    print(john)
    print(repr(john))

    tesla = Admin("Никола", "Тесла", 38, 2, 402)
    print(tesla)
    print(repr(tesla))

    print(f"{john.compare_to(tesla) = }")
    print(f"{tesla.compare_to(john) = }")

    bob = Staff("Bob", "Ross", 40, "Department of Art", "Art Teacher")
    print(bob)
    print(repr(bob))

    jerald = Staff(
        "Jerald",
        "Clark",
        8675309,
        "Department of Jerald",
        "Jerald title",
    )
    print(jerald)
    print(repr(jerald))

    print(f"{bob.equal_to(jerald) = }")
    print(f"{jerald.equal_to(bob) = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
