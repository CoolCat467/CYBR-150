"""Lab 2 - CYBR 150 lab assignment."""

# Programmed by CoolCat467

from __future__ import annotations

# Lab 2 - CYBR 150 lab assignment
# Last modified: 2025/01/29
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

__title__ = "Lab II"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"


from collections import Counter
from pathlib import Path
from typing import Final

ROOT_FOLDER: Final = Path(__file__).absolute().parent


def read_file(path: Path) -> str:
    """Return all lines from file as one string blob."""
    return "".join(path.read_text("utf-8").strip().splitlines())


def ask_path(prompt: str) -> Path:
    """Return path that exists from user input."""
    while True:
        path = ROOT_FOLDER / input(prompt)
        if path.exists():
            return path
        print(f"{str(path)!r} does not exist, please try again.")


def print_counter(counter: Counter[str]) -> None:
    """Print counter data."""
    print("\n".join(f"{char} | {count}" for char, count in counter.items()))


def run() -> None:
    """Run program."""
    text = read_file(ask_path("Please enter the filename: "))
    # Use counter to get mapping of character to number of occurrences
    counts = Counter(text)
    print_counter(counts)


if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    run()
