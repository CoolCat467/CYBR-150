"""Driver - Test class functionality."""

# Programmed by CoolCat467

from __future__ import annotations

# Driver - Test class functionality
# Last modified: 2024/02/13
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


from My_Circle import My_Circle as Circle


def test_circle() -> None:
    """Test circle."""
    t = Circle("jerald", 6)
    assert t.get_name() == "jerald"
    print(t.get_name())
    assert t.get_radius() == 6
    print(t.get_radius())
    print(t)
    print(repr(t))


def main() -> None:
    """Run program."""
    c1 = Circle("c1", 2)
    c2 = Circle("c2", 3)
    c3 = Circle("circle_1", 20)

    print(c1.get_name(), c1.get_radius())
    print(c2.get_name(), c2.get_radius())

    c1.set_name("circle_1")
    c1.set_radius(20)
    print(c1.get_name(), c1.get_radius())

    c2.set_name("circle_2")
    c2.set_radius(30)
    print(c2.get_name(), c2.get_radius())

    print(c1)
    print(c2)
    print(c3)

    print(f"{c1.equal_to(c2) = }")
    print(f"{c2.equal_to(c1) = }")
    print(f"{c1.equal_to(c3) = }")

    print(f"{c1.compare_to(c2) = }")
    print(f"{c2.compare_to(c1) = }")
    print(f"{c1.compare_to(c3) = }")

    print("\n")
    test_circle()


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
