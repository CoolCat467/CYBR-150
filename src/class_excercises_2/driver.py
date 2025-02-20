"""Driver - Test class functionality."""

# Programmed by CoolCat467

from __future__ import annotations

# Driver - Test class functionality
# Last modified: 2024/02/04
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


from airplane import Airplane
from circle import Circle
from rhombus import Rhombus


def test_circle() -> None:
    """Test circle."""
    c = Circle(6)
    assert c.get_radius() == 6
    print(c.get_radius())
    assert c.get_area() == 113.09733552923255
    print(c.get_area())
    print(c)
    print(repr(c))


def test_rhombus() -> None:
    """Test rhombus."""
    r = Rhombus(6, 20, 30)
    assert r.get_side_length() == 6
    print(r.get_side_length())
    assert r.get_diag_1() == 20
    print(r.get_diag_1())
    assert r.get_diag_2() == 30
    print(r.get_diag_2())
    print(r)
    print(repr(r))


def test_airplane() -> None:
    """Test airplane."""
    airplane = Airplane("Никола", "Тесла", 27, 300, 200)
    assert airplane.get_brand() == "Никола"
    print(airplane.get_brand())
    assert airplane.get_model() == "Тесла"
    print(airplane.get_model())
    assert airplane.get_engine_number() == 27
    print(airplane.get_engine_number())
    assert airplane.get_passenger_number() == 300
    print(airplane.get_passenger_number())
    assert airplane.get_top_speed() == 200
    print(airplane.get_top_speed())
    print(airplane)
    print(repr(airplane))


def main() -> None:
    """Run program."""
    test_circle()
    print("------------")
    test_rhombus()
    print("------------")
    test_airplane()


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
