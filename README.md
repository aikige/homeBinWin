%USERPROFILE%\bin scripts for Windows Environment
=================================================

This folder stores utility script which I'm usually using in my Winodws environment.

## Setup

1. Clone

```
pushd %USERPROFILE%
git clone https://github.com/aikige/homeBinWin.git bin
```

2. Open "System Property" dialog in Windows and add %USERPROFILE%\bin
	to `PATH` environment variable.
	Following command can be used to open the dialog.

```
control sysdm.cpl
```

## Important Scripts

### sendToVim.vbs

Script to open files in existing gVim window.
Usually, it is used in shell:sendto entry.

### dumpForegroundWindow.py

A python script to keep log of forground window, in Windows environment.
This script will be convenient if you want to keep logging of your work-time.
