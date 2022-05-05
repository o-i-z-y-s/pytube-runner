# pytube-runner
This is a Python CLI script for downloading individual videos from YouTube. The [pytube](https://github.com/pytube/pytube) project is the core of this runner, so naturally pytube is required for it to function.
EDIT 5/5/22: There is a current bug in pytube breaking functionality. [Here is the fix](https://github.com/pytube/pytube/issues/1293#issuecomment-1103362815), and it requires you to copy-paste a couple of lines into the cipher.py file located in your pytube installation.

## Why?
Typing out function calls in a text editor and pasting them into a CLI is tedious, especially when errors are a blackbox and reinstalling pytube is a common troubleshooting method (for a couple reasons).
This runner solves most of these problems by:
- Chaining the parameters and download functions in one place for easy modification
- Asking the user to provide a video URL and clearly communicating most errors
- Prompting automated reinstallation of pytube if it encounters an AttributeError

## Default Settings
This script downloads progressive MP4 files in the highest resolution available, but only up to 720p. Once ripped, the videos are placed in a folder peer with the script file.
These settings can be changed in the file itself, as you may just want that crunchy 240p aesthetic, or maybe adaptive suits your needs better than progressive.
Check out [the pytube documentation](https://pytube.io/en/latest/) for descriptions of pytube's possible parameters and functions.

## Dependencies
- [Python 3.x](https://www.python.org/downloads/)
- [pytube](https://github.com/pytube/pytube)
- [pip](https://pypi.org/project/pip/)

The included batch file uses pip to install/reinstall pytube for you, which really only saves you one trip to your Terminal, but it's a saved step nonetheless.
