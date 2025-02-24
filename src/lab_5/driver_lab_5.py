"""Driver - Test class functionality."""

# Programmed by CoolCat467

from __future__ import annotations

# Driver - Test class functionality
# Last modified: 2024/02/20
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


from automobile import Automobile
from car import Car
from truck import Truck


def test_automobile() -> None:
    """Test automobile."""
    automobile = Automobile("Make", "Model", 2004, 186, 24)
    assert automobile.get_make() == "Make"
    print(automobile.get_make())
    assert automobile.get_model() == "Model"
    print(automobile.get_model())
    assert automobile.get_year() == 2004
    print(automobile.get_year())
    assert automobile.get_weight() == 186
    print(automobile.get_weight())
    assert automobile.get_acceleration() == 24
    print(automobile.get_acceleration())
    print(automobile)
    print(repr(automobile))


def main() -> None:
    """Run program."""
    test_automobile()
    print("------------")

    a1 = Automobile("Make", "Model", 2004, 186, 24)
    a1.set_make("Ford")
    a1.set_model("Mustang")
    a1.set_year(1966)
    a1.set_weight(1224)
    a1.set_acceleration(25)
    print(
        a1.get_make(),
        a1.get_model(),
        a1.get_year(),
        a1.get_weight(),
        a1.get_acceleration(),
    )

    print("------------")

    a1 = Automobile("Ford", "Mustang", 1966, 1224, 25)
    a2 = Automobile("Chevy", "Camaro", 1969, 1379, 26)
    print(a1)
    print(a2)

    print("------------")

    c1 = Car("Plymouth", "Cuda", 1971, 1478, 27, 2)
    c2 = Car("Ford", "Mustang", 1966, 1224, 25, 2)
    c3 = Car("Chevy", "Camaro", 1969, 1379, 26, 2)
    print(c1)
    print(c2)
    print(c3)

    print("------------")

    c1 = Car("Plymouth", "Cuda", 1971, 1478, 27, 2)
    t1 = Truck("Chevy", "K10", 1984, 2200, 40, 4)
    print(c1)
    print(t1)


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
