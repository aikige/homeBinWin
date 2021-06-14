Setup scripts
=============

This folder contains scripts used to setup scripts in [parent folder](../README.md).

## Note about scripts

### `prepSendTo.bat`

Creates [`sendToVim.vbs`](../sendToVim.vbs) shortcut in `shell:sendto`.

### `prepDisplayUtils.bat`

Creates display related utility shortcuts in `shell:start menu`.

1. Display resolution changer, which uses [`set_screen_resolution.bat`](../set_screen_resolution.bat). 
    * `VGA`
    * `SVGA`
    * `XGA`
    * `Full HD`
1. Display mode changer, wich uses `DisplaySwitch.exe` as its backend.
    * `Display Clone`
    * `Display Extend`

### `prepPath.bat`

Add parent directory to the `PATH` user environment.

Since this script is using PowerShell as backend, please check instruciton regarding [Preparation to use PowerShell Scripts](#preparation-to-use-powershell-scripts).

### `prepLockLogging.bat` and `prepLockLogging.py`

`prepLockLogging.bat` is used to enable logging for Windows Lock and Unlock.

1. This script shall be executed on command prompt with Administrator's privilege.
1. Actual scheduled task registration is implmented by `prepLockLogging.py`.
    * this script depends on `win32com` in [pywin32](https://pypi.org/project/pywin32/) extension.
      If your system dose not have the package, please install it using `pip install pywin32`.

Reference:

* Microsoft TechNet > [Schedule task with trigger "on workstation Lock"](https://social.technet.microsoft.com/Forums/en-US/2263c5a7-41d4-4c64-96ee-46437aba1a85/)
* Microsoft | Docs > [Windows/Apps/Win32/Server Technologies/Windows Server/Task Scheduler/Trigger object](https://docs.microsoft.com/windows/win32/taskschd/trigger)

## Preparation to use PowerShell Scripts

To use PowerShell scripts, you may need to change [Execution Policy](https://docs.microsoft.com/powershell/scripting/learn/ps101/01-getting-started#execution-policy) of PowerShell.

1. Please start powershell with Administrator's privilege.
1. Please check if you are allowed to executed script: `get-executionpolicy`.
1. If result is `Restricted`, enable execution: `set-executionpolicy remotesigned`.

Reference:

* Microsoft | Docs > [Getting Started with PowerShell > Execution Policy](https://docs.microsoft.com/powershell/scripting/learn/ps101/01-getting-started#execution-policy)
