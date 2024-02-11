# pytube-runner
This is a Python script for downloading individual videos from YouTube. This project includes both a standalone EXE as well as the CLI version.

*CLI version only*: The [pytube](https://github.com/pytube/pytube) project is the core of this script, so naturally pytube is required for it to function.

**NOTE:** There is currently a regex bug in pytube causing download failures. However, I have repaired the file responsible and included it in this repo, `cipher.py`. Replace your version of this file with the copy provided; you can find yours at `<Python directory)\Lib\site-packages\pytube>`. [The fix is described here](https://github.com/pytube/pytube/issues/1293#issuecomment-1103362815).

## Why?
Typing out Pytube function calls in a CLI is tedious, especially when errors are a blackbox with this library.

This runner solves many issues:
- Chaining the parameters and download functions in one place for easy modification
- Asking the user to provide a video URL and clearly communicating most errors
- Prompting automated reinstallation of pytube if it encounters an AttributeError (*CLI version only.*)

## Default Settings
This script downloads progressive MP4 files in the highest resolution available, but only up to 720p. Once ripped, the videos are placed in a folder peer with the script file/EXE.

*CLI version only for now*: These settings can be changed in the file itself, as you may just want that crunchy 240p aesthetic, or maybe adaptive suits your needs better than progressive.

Check out [the pytube documentation](https://pytube.io/en/latest/) for descriptions of pytube's possible parameters and functions.

## Dependencies
*CLI version only.* The EXE version has no dependencies.
- [Python 3.x](https://www.python.org/downloads/)
- [pytube](https://github.com/pytube/pytube)
- [customtkinter](https://github.com/tomschimansky/customtkinter)
- [pip](https://pypi.org/project/pip/)

The included batch file uses pip to install/reinstall pytube for you, which really only saves you one trip to your terminal, but it's a saved step nonetheless.

## Known Issues
These are not problems with this script, but rather issues upstream in Pytube itself.
- Playlists come in as empty.
- Whole channels similarly come in empty.
- Authenticating yourself to download Age Restricted videos is not working.