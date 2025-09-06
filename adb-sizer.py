import sqlite3
from typing import Tuple
import subprocess
import os

type ConfigType = Tuple[str, int, int]


def main():
    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    db_path: str = os.path.join(script_dir, "adb-sizer.db")

    con: sqlite3.Connection = sqlite3.connect(db_path)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS config(name, width, height)")

    done: bool = False
    while not done:
        print("[1] Add a new configuration")
        print("[2] Select configuration")
        print("[3] Exit")
        try:
            option: int = read_int("> ", 1, 3)
        except KeyboardInterrupt:
            print()
            option = 3

        match option:
            case 1:
                print("Use Ctrl+C to come back to the menu.")
                try:
                    name: str = input("Insert the name for the new configuration: ")
                    width: int = read_int(
                        "Insert the width for the new configuration: ", 1, 999999
                    )
                    height: int = read_int(
                        "Insert the height for the new configuration: ", 1, 999999
                    )

                    cur.execute(
                        "INSERT INTO config VALUES(?, ?, ?)", (name, width, height)
                    )
                    con.commit()
                except KeyboardInterrupt:
                    print()
            case 2:
                try:
                    res: sqlite3.Cursor = cur.execute("SELECT * FROM config")
                    configs: list[ConfigType] = res.fetchall()
                    len_configs: int = len(configs)

                    if len_configs == 0:
                        print("You must create a configuration before applying it.")
                    else:
                        for i, config in enumerate(configs):
                            print(f"[{i}] {config[0]} ({config[1]}x{config[2]})")
                        print(f"[{len_configs}] Nevermind")

                        option = read_int("> ", 0, len_configs)
                        if option != len_configs:
                            config = configs[option]
                            subprocess.run(
                                [
                                    "adb",
                                    "shell",
                                    "wm",
                                    "size",
                                    f"{config[1]}x{config[2]}",
                                ]
                            )
                except KeyboardInterrupt:
                    print()
            case 3:
                done = True
                print("Have a great day!")


def read_int(text: str, min: int, max: int) -> int:
    success: bool = False
    read: int = -1

    while not success:
        try:
            read = int(input(text))
            success = read >= min and read <= max
            if not success:
                print(f"The number must be between {min} and {max}.")
        except ValueError:
            print("You must insert an integer.")

    return read


if __name__ == "__main__":
    main()
