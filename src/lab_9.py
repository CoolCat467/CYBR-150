"""Lab 9 - Caesar cipher 'encrypted' file editor."""

# Programmed by CoolCat467

from __future__ import annotations

# Lab 9 - Caesar cipher 'encrypted' file editor
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

__title__ = "CryptoPad"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"

import os
import tkinter as tk
import traceback
from functools import partial
from pathlib import Path
from tkinter import filedialog
from typing import Final

GEO: Final = "900x600"


###################################################################################
#
# Instructions!
#
# Please start at Step 1 and progress through each step. If you need help, see the
# Companion lab document and refer back to lab 11. This is problem solving, please
# give your best effort to each solution.
#
###################################################################################


# Callbacks
def save_file(root: tk.Tk) -> None:
    """Save current text contents 'encrypted' to a file."""
    filename = filedialog.asksaveasfilename(
        parent=root,
        initialdir=os.getcwd(),
        title="Save",
    )
    if not filename:
        return
    path = Path(filename).absolute()
    # Step 19 - If ".txt" is not in the file, add it to the end of filename
    text = root.children["!text"]
    assert isinstance(text, tk.Text)
    content = text.get("1.0", tk.END)
    # Step 20 - call the encrypt function with content as the argument, save result to a variable called enc
    encoded = encrypt(root, content)
    # Step 21 - write enc to the file chosen above (filename)
    path.write_text(encoded, encoding="utf-8")
    # Step 22 - Call the clear() function
    text.insert("1.0", "Saved")
    text.after(400, partial(clear, root))
    # Step 23 - Go back to main


def open_file(root: tk.Tk) -> None:
    """Open and decode 'encrypted' file."""
    print("Open")
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Open",
    )
    if not filename:
        return
    path = Path(filename).absolute()

    content = ""

    text = root.children["!text"]
    assert isinstance(text, tk.Text)

    text.delete("1.0", tk.END)
    try:
        content = "".join(path.read_text(encoding="utf-8").splitlines())
        cleartext = decrypt(root, content)
    except Exception as exc:
        print("Error opening")
        traceback.print_exception(exc)
        cleartext = "Please choose a file."
    text.insert("1.0", cleartext)


def decrypt(root: tk.Tk, cipher: str) -> str:
    """'Decrypt' and return plaintext."""
    frame_2 = root.children["!frame2"]
    assert isinstance(frame_2, tk.Frame)

    frame_2_text = frame_2.children["!text"]
    assert isinstance(frame_2_text, tk.Text)

    root_text = root.children["!text"]
    assert isinstance(root_text, tk.Text)

    key = str(
        frame_2_text.get("1.0", tk.END),
    ).strip()
    output = ""
    if not key:
        root_text.insert("1.0", "ENTER A KEY!")
    else:
        key_int = int(key)
        for char in cipher:
            s = chr(ord(char) - key_int)
            output += s
    return output


def encrypt(root: tk.Tk, cleartext: str) -> str:
    """'Encrypt' and return cipher text."""
    frame_2 = root.children["!frame2"]
    assert isinstance(frame_2, tk.Frame)

    frame_2_text = frame_2.children["!text"]
    assert isinstance(frame_2_text, tk.Text)

    key = str(
        frame_2_text.get("1.0", tk.END),
    )
    output = ""
    for char in cleartext.strip():
        s = chr(ord(char) + int(key))
        output += s
        print(str(char) + " ---> " + str(s))
    frame_2_text.delete("1.0", tk.END)
    return output


def clear(root: tk.Tk) -> None:
    """Clear text instance."""
    print("Clear")

    text = root.children["!text"]
    assert isinstance(text, tk.Text)

    text.delete("1.0", tk.END)


def init(root: tk.Tk) -> None:
    """Set title and geometry."""
    # Step 2 - Set title to "CryptoPad - {Your Name Here}"
    root.title(f"{__title__} - {__author__}")
    # Step 3 - Set geometry to the global variable GEO
    root.geometry(GEO)
    # Return to Main, look for Step 4


def get_buttons(
    root: tk.Tk,
    button_frame: tk.Frame,
) -> tuple[tk.Button, tk.Button, tk.Button]:
    """Create and return buttons in button frame."""
    # Step 9 - Make a new button called save_btn: parent is button_frame, text is "Save", command is save_file
    save_btn = tk.Button(
        button_frame,
        text="Save",
        command=partial(save_file, root),
    )
    # Step 10 - Make a new button called open_btn: parent is button_frame, text is "Open, command is open_file
    open_btn = tk.Button(
        button_frame,
        text="Open",
        command=partial(open_file, root),
    )
    # Step 11 - Make a new button called clear_btn" parent is button_frame, text is "Clear", command is clear
    clear_btn = tk.Button(
        button_frame,
        text="Clear",
        command=partial(clear, root),
    )
    # Go back to set_content and look for Step 12
    return save_btn, open_btn, clear_btn


def get_button_frame(
    root: tk.Tk,
) -> tuple[tk.Frame, tk.Button, tk.Button, tk.Button]:
    """Create and return button frame and buttons."""
    # Step 6 - Make a new tkinter.Frame with root as the parent and call it button_frame
    button_frame = tk.Frame(root)
    # Step 7 - Call the .pack() function with args (fill=X, side=tkinter.TOP)
    button_frame.pack(fill=tk.X, side=tk.TOP)
    # Step 8 - Go to get_buttons()
    save_btn, open_btn, clear_btn = get_buttons(root, button_frame)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
    return button_frame, save_btn, open_btn, clear_btn


def get_textarea(root: tk.Tk) -> tk.Text:
    """Create and return text area."""
    width, height = GEO.split("x", 1)
    h_lines = int(height) // 8
    w_chars = int(width) // 8
    return tk.Text(root, height=h_lines, width=w_chars)


def get_key_frame(
    root: tk.Tk,
) -> tuple[tk.Frame, tk.Text, tk.Label]:
    """Create and return key frame, key frame text, and key frame label."""
    # Step 13 - Make a new tkinter.Frame called key_frame, parent is root
    key_frame = tk.Frame(root)
    # Step 14 - Call the .pack() method on the key_frame variable with args (fill=X, side=BOTTOM)
    key_frame.pack(fill=tk.X, side=tk.BOTTOM)
    # Step 15 - Create a tkinter.Text object called key_area, parent is key_frame, height=1
    key_area = tk.Text(key_frame, height=1)
    # Step 16 - Create a tkinter.Label object called label, parent is key_frame, text is "Enter Encryption Integer: "
    label = tk.Label(key_frame, text="Enter Encryption Integer: ")
    key_frame.columnconfigure(0, weight=1)
    key_frame.columnconfigure(1, weight=1)
    # Go back to set_content(), look for Step 17
    return key_frame, key_area, label


def grid_widgets(
    save_btn: tk.Button,
    open_btn: tk.Button,
    clear_btn: tk.Button,
    text: tk.Text,
    key_area: tk.Text,
    label: tk.Label,
) -> None:
    """Grid widgets."""
    save_btn.grid(row=0, column=0, sticky=tk.W + tk.E)
    open_btn.grid(row=0, column=1, sticky=tk.W + tk.E)
    clear_btn.grid(row=0, column=2, sticky=tk.W + tk.E)
    label.grid(row=0, column=0, sticky=tk.W + tk.E)
    key_area.grid(row=0, column=1, sticky=tk.W + tk.E)
    text.pack(side=tk.TOP)


def set_content(root: tk.Tk) -> tk.Tk:
    """Configure window."""
    # Step 5 - Go to get_button_frame()
    button_frame, save_btn, open_btn, clear_btn = get_button_frame(root)
    text = get_textarea(root)
    # Step 12 - Go to get_key_frame()
    key_frame, keyarea, label = get_key_frame(root)
    # Step 17 - Go back to main, look for Step 18
    grid_widgets(save_btn, open_btn, clear_btn, text, keyarea, label)
    return root


def main() -> None:
    """Run program."""
    root = tk.Tk()

    # Step 1 - Go to init() function
    init(root)

    # Step 4 - Go to set_content() function
    set_content(root)
    # Step 18 - Go to the save_file() function
    # Step 24 - Run the program... see if it works!
    root.mainloop()


if __name__ == "__main__":
    main()
