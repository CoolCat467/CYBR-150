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


from admin import Admin
from appliance import Appliance
from bedroom import Bedroom
from dishwasher import Dishwasher
from employee import Employee
from freezer import Freezer
from garage import Garage
from kitchen import Kitchen
from refrigerator import Refrigerator
from room import Room
from student import Student
from user import User


def test_user() -> None:
    """Test user."""
    user = User("John", "Von Neumann")
    assert user.get_first_name() == "John"
    print(user.get_first_name())
    assert user.get_last_name() == "Von Neumann"
    print(user.get_last_name())
    print(user)
    print(repr(user))


def test_student() -> None:
    """Test student."""
    student = Student("Jerald", "Clark", "8675309")
    assert student.get_first_name() == "Jerald"
    print(student.get_first_name())
    assert student.get_last_name() == "Clark"
    print(student.get_last_name())
    assert student.get_student_id() == "8675309"
    print(student.get_student_id())
    print(student)
    print(repr(student))


def test_employee() -> None:
    """Test employee."""
    e = Employee("Bob", "Ross", "Art Teacher")
    assert e.get_first_name() == "Bob"
    print(e.get_first_name())
    assert e.get_last_name() == "Ross"
    print(e.get_last_name())
    assert e.get_position_title() == "Art Teacher"
    print(e.get_position_title())
    print(e)
    print(repr(e))


def test_admin() -> None:
    """Test admin."""
    admin = Admin("Никола", "Тесла", "Scientist", 27)
    assert admin.get_first_name() == "Никола"
    print(admin.get_first_name())
    assert admin.get_last_name() == "Тесла"
    print(admin.get_last_name())
    assert admin.get_position_title() == "Scientist"
    print(admin.get_position_title())
    assert admin.get_security_level() == 27
    print(admin.get_security_level())
    print(admin)
    print(repr(admin))


def test_room() -> None:
    """Test room."""
    room = Room(4, 3)
    assert room.get_width() == 4
    print(room.get_width())
    assert room.get_length() == 3
    print(room.get_length())
    print(room)
    print(repr(room))


def test_kitchen() -> None:
    """Test kitchen."""
    kitchen = Kitchen(3, 23, "Hitachi")
    assert kitchen.get_width() == 3
    print(kitchen.get_width())
    assert kitchen.get_length() == 23
    print(kitchen.get_length())
    assert kitchen.get_appliance_brand() == "Hitachi"
    print(kitchen.get_appliance_brand())
    print(kitchen)
    print(repr(kitchen))


def test_bedroom() -> None:
    """Test bedroom."""
    bedroom = Bedroom(6, 8, "lime green")
    assert bedroom.get_width() == 6
    print(bedroom.get_width())
    assert bedroom.get_length() == 8
    print(bedroom.get_length())
    assert bedroom.get_color() == "lime green"
    print(bedroom.get_color())
    print(bedroom)
    print(repr(bedroom))


def test_garage() -> None:
    """Test garage."""
    garage = Garage(24, 48, 79)
    assert garage.get_width() == 24
    print(garage.get_width())
    assert garage.get_length() == 48
    print(garage.get_length())
    assert garage.get_bay_numbers() == 79
    print(garage.get_bay_numbers())
    print(garage)
    print(repr(garage))


def test_appliance() -> None:
    """Test appliance."""
    appliance = Appliance("Generic", "General Electric")
    assert appliance.get_type() == "Generic"
    print(appliance.get_type())
    assert appliance.get_brand() == "General Electric"
    print(appliance.get_brand())
    print(appliance)
    print(repr(appliance))


def test_dishwasher() -> None:
    """Test dishwasher."""
    dishwasher = Dishwasher("Dishwasher", "Bosch", 120)
    assert dishwasher.get_type() == "Dishwasher"
    print(dishwasher.get_type())
    assert dishwasher.get_brand() == "Bosch"
    print(dishwasher.get_brand())
    assert dishwasher.get_capacity() == 120
    print(dishwasher.get_capacity())
    print(dishwasher)
    print(repr(dishwasher))


def test_refrigerator() -> None:
    """Test refrigerator."""
    refrigerator = Refrigerator("Refrigerator", "Samsung", 84)
    assert refrigerator.get_type() == "Refrigerator"
    print(refrigerator.get_type())
    assert refrigerator.get_brand() == "Samsung"
    print(refrigerator.get_brand())
    assert refrigerator.get_volume() == 84
    print(refrigerator.get_volume())
    print(refrigerator)
    print(repr(refrigerator))


def test_freezer() -> None:
    """Test freezer."""
    freezer = Freezer("Freezer", "Amana", -20)
    assert freezer.get_type() == "Freezer"
    print(freezer.get_type())
    assert freezer.get_brand() == "Amana"
    print(freezer.get_brand())
    assert freezer.get_low_temp() == -20
    print(freezer.get_low_temp())
    print(freezer)
    print(repr(freezer))


def main() -> None:
    """Run program."""
    test_user()
    print("------------")
    test_student()
    print("------------")
    test_employee()
    print("------------")
    test_admin()
    print("------------")
    test_room()
    print("------------")
    test_kitchen()
    print("------------")
    test_bedroom()
    print("------------")
    test_garage()
    print("------------")
    test_appliance()
    print("------------")
    test_dishwasher()
    print("------------")
    test_refrigerator()
    print("------------")
    test_freezer()


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
