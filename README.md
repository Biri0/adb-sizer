# adb-sizer

A tiny interactive utility to speed up preparing Android phone screenshots for the
Play Store by applying named screen-size presets to a connected device using ADB.

## Purpose

`adb-sizer.py` lets you store named width×height presets and quickly apply them to
a connected Android device via:

`adb shell wm size <WIDTHxHEIGHT>`

This is useful when you need to produce screenshots with specific dimensions (for
example, Play Store screenshot sizes) and want a fast, repeatable way to switch the
device resolution.

## Requirements

- Python 3
- `adb` (Android Debug Bridge) available in your PATH and a device connected or an
  emulator running
- Permission to create files in the directory where you run the script (it creates
  an SQLite DB named `adb-sizer.db`)

## Installation

You can run the script directly with Python:

`python adb-sizer.py`

To make it convenient to run from anywhere, you can add a shell alias (example for
`~/.bashrc` or `~/.zshrc`):

```bash
# Add this line to your shell rc file (adjust the path to where you store the script)
alias adbsizer='python3 /full/path/to/adb-sizer/adb-sizer.py'
```

## Usage

When you run `adb-sizer.py` you get a simple interactive menu:

- Add a new configuration: provide a name, width and height (integers).
- Select configuration: pick a preset and the script runs `adb shell wm size <WIDTHxHEIGHT>`.
- Exit

Notes:

- Use Ctrl+C while entering values to cancel and return to the menu.
- Presets are persisted in `adb-sizer.db` in the directory where the code lives.
- The script does not currently revert screen size automatically; to restore the
  device to its default size run:

`adb shell wm size reset`

## Example workflow

1. Start the script:
   `python adb-sizer.py` (or `adbsizer` if you added an alias)
2. Add a configuration named "Play-1080x1920" with width `1080` and height `1920`.
3. Select that configuration to apply the resolution to your connected device.
4. Take screenshots with your preferred tooling (e.g.,
   `adb exec-out screencap -p > screenshot.png`).
5. When finished, reset the device size if needed:
   `adb shell wm size reset`

## Implementation notes

- Presets are stored in a local SQLite database file `adb-sizer.db`.
- The script executes the `adb` command via `subprocess.run`, so ensure the device
  is visible to `adb` (check `adb devices`).

## Contributing

This project is small and focused. If you want to contribute:

- Open issues or PRs for enhancements (examples: non-interactive CLI mode, preset
  import/export, automatic reset).
- Keep changes well-documented and linted.

## License

This project is released under the [MIT](LICENSE) License.

## Acknowledgements

Created to speed up Play Store screenshot workflows by Mariano Riefolo.

