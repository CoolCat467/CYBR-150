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


from animal import Animal
from employee_class_exercises import Employee
from house import House
from rectangle import Rectangle
from student_class_exercises import Student
from triangle import Triangle


def test_triangle() -> None:
    """Test triangle."""
    t = Triangle(6, 20)
    assert t.get_height() == 6
    print(t.get_height())
    assert t.get_length() == 20
    print(t.get_length())
    print(t)
    print(repr(t))


def test_rectangle() -> None:
    """Test rectangle."""
    r = Rectangle(6, 20)
    assert r.get_height() == 6
    print(r.get_height())
    assert r.get_length() == 20
    print(r.get_length())
    print(r)
    print(repr(r))


def test_student() -> None:
    """Test student."""
    student = Student("Никола", "Тесла", "<unknown>", "1856/07/10")
    assert student.get_first_name() == "Никола"
    print(student.get_first_name())
    assert student.get_middle_name() == "<unknown>"
    print(student.get_middle_name())
    assert student.get_last_name() == "Тесла"
    print(student.get_last_name())
    assert student.get_birthday() == "1856/07/10"
    print(student.get_birthday())
    print(student)
    print(repr(student))


def test_employee() -> None:
    """Test employee."""
    employee = Employee(
        "8675309",
        "CoolCats",
        "Mcjerald",
        "CoolCat467@duck.com",
    )
    assert employee.get_employee_id() == "8675309"
    print(employee.get_employee_id())
    assert employee.get_first_name() == "CoolCats"
    print(employee.get_first_name())
    assert employee.get_last_name() == "Mcjerald"
    print(employee.get_last_name())
    assert employee.get_email() == "CoolCat467@duck.com"
    print(employee.get_email())
    print(employee)
    print(repr(employee))


def test_animal() -> None:
    """Test animal."""
    animal = Animal("Felius Catus", 4, 18, "Fred")
    assert animal.get_type() == "Felius Catus"
    print(animal.get_type())
    assert animal.get_legs() == 4
    print(animal.get_legs())
    assert animal.get_size() == 18
    print(animal.get_size())
    assert animal.get_name() == "Fred"
    print(animal.get_name())
    print(animal)
    print(repr(animal))


def test_house() -> None:
    """Test house."""
    house = House(5, 3, 2_126, 12_438.76)
    assert house.get_num_rooms() == 5
    print(house.get_num_rooms())
    assert house.get_num_bathrooms() == 3
    print(house.get_num_bathrooms())
    assert house.get_total_square_foot() == 2_126
    print(house.get_total_square_foot())
    assert house.get_current_price() == 12_438.76
    print(house.get_current_price())
    print(house)
    print(repr(house))


def main() -> None:
    """Run program."""
    test_triangle()
    print("------------")
    test_rectangle()
    print("------------")
    test_student()
    print("------------")
    test_employee()
    print("------------")
    test_animal()
    print("------------")
    test_house()


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
