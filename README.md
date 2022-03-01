# pytube-runner
This is a Python CLI script for downloading individual videos from YouTube. The [pytube](https://github.com/pytube/pytube) project is the core of this runner, so naturally pytube is required for it to function.

## Why?
Typing out function calls in a text editor and pasting them into a CLI is tedious, especially when errors are a blackbox and reinstalling pytube is a common troubleshooting method for various reasons.
This runner solves most of these problems by:
- Chaining the parameters and download functions in one place for easy modification
- Asking the user to provide a video URL and clearly communicating most errors
- Prompting automated reinstallation of pytube if it encounters an AttributeError

## Defaults
This script downloads progressive MP4 files in the highest resolution available (up to 720p). Once ripped, the videos are placed in a folder peer with the script file.
Check out [the pytube documentation](https://pytube.io/en/latest/) for descriptions of pytube's possible parameters.

## Dependencies
- [Python 3.x](https://www.python.org/downloads/)
- [pytube](https://github.com/pytube/pytube)
The included batch file can install/reinstall pytube for you, which really only saves you one trip to your Terminal, but it's a saved step nonetheless.