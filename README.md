%USERPROFILE%\bin scripts for Windows Environment
=================================================

This folder stores utility script which I'm usually using
in my Windows environment.

## Setup

1. Clone

```
pushd %USERPROFILE%
git clone https://github.com/aikige/homeBinWin.git bin
```

2. Add `%USERPROFILE%\bin` to `PATH` environment variable.
    There is script for the preparation, in `setup` directory.

```
cd setup
prepPath.bat
```

## Important Scripts

### `sendToVim.ps1`

Script to open files in existing [GVim](https://www.vim.org/) window.
Usually, it is used as `shell:sendto` entry in Windows system.

### `dumpForegroundWindow.pyw`

```text
usage: dumpForegroundWindow.pyw [-h] [-k] [-i INTERVAL] [-s] [-v] [message]

positional arguments:
  message               addtional message stored with window title

options:
  -h, --help            show this help message and exit
  -k, --keep_logging    if this argument is set, keep logging
  -i INTERVAL, --interval INTERVAL
                        set interval of logging in seconds. default interval is 120
  -s, --skip_duplicate  if this argument is set, skip logging of duplicated title
  -v, --verbose         show log to standard output also
```

The script captures foreground window title and stores it to the log file.

When script is started with `--keep_logging` option,
it keeps logging of foreground window title,
with interval specified by `--interval` option.
This script will be convenient if you want to keep logging of your work-time.

Other notes about features:

* This scripts depends on [pywin32](https://pypi.org/project/pywin32/) package.
	If your system does not have the package, please install it.
    ```
    pip install pywin32
    ```
* Log uses markdown format.
* Log filename is `YYYYMMDD-Window_Log.md`,
	created on the working directory of the script,
	and log file is changed every day.

### `createShortcut.ps1`

Script to crate shortcut. Usually used in batch file.

### `addUserPath.ps1`

Script to add a path to user's `PATH` environment variable.
For example:

```
powershell addUserPath.ps1 %SOME_DIR%
```

will add `%SOME_DIR%` to `PATH`, if `PATH` does not include `%SOME_DIR%`.
