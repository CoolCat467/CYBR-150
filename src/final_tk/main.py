"""Login System - Grab login credentials."""

# Programmed by CoolCat467

from __future__ import annotations

# Login System - Grab login credentials
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

__title__ = "Login System"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__license__ = "GNU General Public License Version 3"


from functools import partial
from os import getenv, makedirs, path
from pathlib import Path
from tkinter import Button, Entry, Label, Tk, Toplevel
from typing import Final

import reader
import security

HOME: Final = Path(getenv("HOME", path.expanduser("~")))
XDG_DATA_HOME: Final = Path(
    getenv("XDG_DATA_HOME", HOME / ".local" / "share"),
)
XDG_CONFIG_HOME: Final = Path(getenv("XDG_CONFIG_HOME", HOME / ".config"))

FILE_TITLE: Final = __title__.lower().replace(" ", "-").replace("-", "_")
CONFIG_PATH: Final = XDG_CONFIG_HOME / FILE_TITLE
DATA_PATH: Final = XDG_DATA_HOME / FILE_TITLE
CREDENTIALS: Final = CONFIG_PATH / "credentials.bi"

PEPPER = "global pepper is important for secure password security"


def handle_signup(
    info_label: Label,
    first_entry: Entry,
    middle_entry: Entry,
    last_entry: Entry,
    email_entry: Entry,
) -> None:
    """Handle signup."""
    first = first_entry.get()
    middle = middle_entry.get()
    last = last_entry.get()
    email = email_entry.get()
    print(f"{first = }\n{middle = }\n{last = }\n{email = }")

    info_label.config(text=f"Welcome {first}!")


def open_new_user_model(root: Tk) -> None:
    """Handle opening new user model."""
    top = Toplevel(root)

    info_label = Label(top, text="You are a New User!")

    first_label = Label(top, text="First")
    first_entry = Entry(top)

    middle_label = Label(top, text="Middle")
    middle_entry = Entry(top)

    last_label = Label(top, text="Last")
    last_entry = Entry(top)

    email_label = Label(top, text="Email")
    email_entry = Entry(top)

    button = Button(
        top,
        text="Signup",
        command=partial(
            handle_signup,
            info_label,
            first_entry,
            middle_entry,
            last_entry,
            email_entry,
        ),
    )

    info_label.grid(row=0, column=0)

    first_label.grid(row=1, column=0)
    first_entry.grid(row=1, column=1)

    middle_label.grid(row=2, column=0)
    middle_entry.grid(row=2, column=1)

    last_label.grid(row=3, column=0)
    last_entry.grid(row=3, column=1)

    email_label.grid(row=4, column=0)
    email_entry.grid(row=4, column=1)

    button.grid(row=5, column=1)


def check_login(username: str, password: str) -> bool:
    """Return True if login credentials are valid from credentials file."""
    username_bytes = username.encode("utf-8")
    with open(CREDENTIALS, "rb") as fp:
        with reader.BiReader(fp) as bi_reader:
            for item in bi_reader:
                if item.name == username_bytes and security.compare_hash_sync(
                    password,
                    item.content.decode("utf-8"),
                    PEPPER,
                ):
                    return True
    return False


def handle_login(
    root: Tk,
    username_entry: Entry,
    password_entry: Entry,
) -> None:
    """Handle login button press."""
    username = username_entry.get()
    password = password_entry.get()
    print(f"[handle_login]\n{username = }\n{password = }\n")

    if check_login(username, password):
        print("Successful login")
        open_new_user_model(root)


def register_new_login(username: str, password: str) -> None:
    """Register new login credentials."""
    print(f"Creating new user {username!r} with password {password!r}")
    with CREDENTIALS.open("ab") as fp:
        fp.write(
            reader.BlobField(
                username.encode("utf-8"),
                security.create_new_login_credentials(
                    password,
                    PEPPER,
                ).encode("utf-8"),
            ).to_stream(),
        )


def main() -> None:
    """Run program."""
    if not path.exists(CONFIG_PATH):
        makedirs(CONFIG_PATH)
    print(f"Credentials file: {CREDENTIALS}")
    if not CREDENTIALS.exists():
        username = "admin"
        password = security.create_new_password(16)
        print("This will only print one time, please record it.")
        register_new_login(username, password)

    root = Tk()

    root.title(f"{__title__} v{__version__}")
    root.geometry("250x100")

    ##
    username_label = Label(root, text="Username")
    username_entry = Entry(root)

    password_label = Label(root, text="Password")
    password_entry = Entry(root, show="*")

    button = Button(
        root,
        text="Login",
        command=partial(handle_login, root, username_entry, password_entry),
    )

    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)

    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)

    button.grid(row=2, column=1)

    # main tkinter's main event loop
    root.mainloop()


if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    main()
