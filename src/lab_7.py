"""Lab 7 - Tkinter GUI test."""

# Programmed by CoolCat467

from __future__ import annotations

# Lab 7 - Tkinter GUI test
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

__title__ = "Lab 7: My several hundreth GUI"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"


from tkinter import Button, Label, Text, Tk


def get_info(text: Text, label: Label) -> None:
    """Write contents of text object's first line to label.

    Only first line because label can't render multiline strings.
    """
    # print("Text")

    # text = cast(Text, root.children["!text"])
    # label = cast(Label, root.children["!label"])

    # Get text
    string = text.get("1.0", "2.0").strip()
    label.configure(text=string)


def main() -> None:
    """Run program."""
    root = Tk()

    root.title(__title__)
    root.geometry("400x400")

    button = Button(root, text="Get", command=lambda: get_info(text, label))
    text = Text(root, height=20, width=100)
    label = Label(root, text="Nothing")

    # Don't pack until `text` and `label` are defined to avoid race
    # condition wherein user clicks get info button before
    # text and label are defined yet.
    button.pack()
    text.pack()
    label.pack()

    # main tkinter's main event loop
    root.mainloop()


if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    main()
