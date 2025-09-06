# adb-sizer

A tiny interactive utility to speed up preparing Android phone screenshots for the
Play Store by applying named screen-size presets to a connected device using ADB.

## Purpose

`adb-sizer.py` lets you store named width×height presets and quickly apply them to
a connected Android device via:

`adb shell wm size <WIDTHxHEIGHT>`

This version also includes a built-in screenshot option that captures the device
screen and saves a PNG locally using `adb exec-out screencap -p`.

## Requirements

- Python 3.12+
  - The code uses the modern `type` alias syntax and other typing features that require
    Python 3.12 or newer.
- `adb` (Android Debug Bridge) available in your PATH and a device connected or an
  emulator running.
- Permission to create files in the directory where you run the script (it creates
  an SQLite DB named `adb-sizer.db` and a `screenshots/` directory when saving screenshots).

## Installation

Run the script directly with Python:

`python3 adb-sizer.py`

(Optional) Add a shell alias to run it conveniently from anywhere (add to `~/.bashrc`
or `~/.zshrc`):

```bash
# Add this line to your shell rc file (adjust the path to where you store the script)
alias adbsizer='python3 /full/path/to/adb-sizer/adb-sizer.py'
```

## Usage

When you run `adb-sizer.py` you get a simple interactive menu:

1. Add a new configuration
   - Provide a name, width and height (integers). Presets are stored in `adb-sizer.db`.
2. Select configuration
   - Pick a preset and the script runs `adb shell wm size <WIDTHxHEIGHT>` to apply
     it.
3. Reset screen size
   - Runs `adb shell wm size reset` to restore the device default size.
4. Screenshot
   - Captures the device screen using `adb exec-out screencap -p` and saves the PNG
     into `screenshots/` with a timestamped filename.
5. Exit

Notes:

- Use Ctrl+C while entering values to cancel and return to the menu.
- Presets are persisted in `adb-sizer.db` in the directory where the script lives.
- The screenshot filename format is generated from the current datetime.

## Example workflow

1. Start the script:
   `python adb-sizer.py` (or `adbsizer` if you added an alias)
2. Add a configuration named "Play-1080x1920" with width `1080` and height `1920`.
3. Select that configuration to apply the resolution to your connected device.
4. Use the "Screenshot" menu option to save a PNG into the `screenshots/` folder.
5. When finished, reset the device size if needed with the "Reset screen size" option.

## Implementation notes

- Presets are stored in a local SQLite database file `adb-sizer.db` (table `config`).
- The script executes `adb` commands via `subprocess.run`, so ensure the device is
  visible to `adb` (check `adb devices`).
- The screenshot feature captures raw PNG bytes from `adb exec-out screencap -p`
  and writes them into the `screenshots/` directory. If the capture fails, the script
  prints the error returned by `adb`.

## Contributing

This project is small and focused. If you want to contribute:

- Open issues or PRs for enhancements (examples: non-interactive CLI mode, preset
  import/export, automatic reset).
- Keep changes well-documented and linted.

## License

This project is released under the [MIT](LICENSE) License.

## Acknowledgements

Created to speed up Play Store screenshot workflows by Mariano Riefolo.
