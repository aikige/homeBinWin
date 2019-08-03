%HOMEPATH%\bin folder for Windows Environment
=============================================

This folder stores utility script which I'm usually using in my Winodws environment.

## Setup

1. Clone

	```
pushd %HOMEPATH%
git clone https://github.com/aikige/homeBinWin.git bin
```

1. Open "System Property" dialog in Windows and add %HOMEPATH%\bin
	to `PATH` environment variable.
	Following command can be used to open the dialog.

	```
control sysdm.cpl
```
