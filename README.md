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

2. Open "System Property" dialog in Windows and add `%USERPROFILE%\bin`
	to `PATH` environment variable.
	Following command can be used to open the dialog.

```
control sysdm.cpl
```

## Important Scripts

### `sendToVim.vbs`

Script to open files in existing [GVim](https://www.vim.org/) window.
Usually, it is used as `shell:sendto` entry in Windows system.

### `dumpForegroundWindow.py`

```
usage: dumpForegroundWindow.py [-h] [-i INTERVAL] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        set interval of logging in seconds. default interval is 120
  -s, --skip_duplicate  if this argument is set, title is logged only when it is different from previous log.
```

A python script to keep log of foreground window title, in Windows environment.
This script will be convenient if you want to keep logging of your work-time.

Other notes about features:


* This scripts depends on [pywin32](https://pypi.org/project/pywin32/) package.
	If your system dose not have the package, please install it using `pip install pywin32`.
* Log uses markdown format.
* Log filename is `YYYYMMDD-Window_Log.md`,
	created on the working directory of the script,
	and log file is changed every day.

### `createShortcut.vbs`

Script to crate shortcut. Usually used in batch file.
