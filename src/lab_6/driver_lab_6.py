"""Driver - Test class functionality."""

# Programmed by CoolCat467

from __future__ import annotations

# Driver - Test class functionality
# Last modified: 2024/02/24
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


from car import Car


def get_to_speed(car: Car, speed: float) -> None:
    """Get up to speed."""
    for x in range(int(speed / car.get_acceleration()) + 1):
        car.accelerate(x)


def go_x_miles(car: Car, distance: int) -> None:
    """Go distance."""
    for _ in range(distance):
        car.move()


def brake_to_speed(car: Car, speed: float) -> None:
    """Brake to speed."""
    for _ in range(
        int((car.get_cur_speed() - speed) / car.get_deceleration()),
    ):
        car.brake()


def take_a_trip() -> None:
    """Simulate car trip."""
    # Start the simulation
    print("\n***** Starting Simulation *****\n")
    owner = input("\tWhat is your name?\n> ")
    max_speed = int(input("\tWhat is the max speed of your car (in MPH)?\n> "))
    print(f"\n***** Creating Car for {owner} *****\n")
    c1 = Car(owner=owner, max_speed=max_speed)

    # Accelerate to speed
    speed = float(
        input("\tWhat speed do you want to accelerate to (in MPH)?\n> "),
    )
    print(f"\n***** Accelerating To {speed} MPH *****\n")
    get_to_speed(c1, speed)

    # Drive a distance
    d1 = int(input("\tHow far do you want to go (in Miles)?\n> "))
    print(f"\n***** Driving {d1} Miles *****\n")
    go_x_miles(c1, d1)

    # Slow down
    brake_speed = float(
        input("\tWhat speed would you like to brake to (in MPH)?\n> "),
    )
    print(f"\n***** Decelerating To {brake_speed} MPH *****\n")
    brake_to_speed(c1, brake_speed)

    # Drive a bit further
    d2 = int(
        input("\tHow far would you like to go at this speed (in Miles)?\n> "),
    )
    print(f"\n***** Driving {d2} Miles *****\n")
    go_x_miles(c1, d2)

    # End trip
    print("***** Trip Over! Braking to Zero MPH *****")
    brake_to_speed(c1, 0)

    # Print Trip Summary
    print("\nTRIP SUMMARY:\n")
    print(c1)


def main() -> None:
    """Run program."""
    take_a_trip()


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    main()
