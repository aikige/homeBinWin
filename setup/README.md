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

### `prepLockLogging.bat`

Script to enable logging for Windows Lock and Unlock.

This script shall be executed on command prompt with Administrator's privilege.

This script works on Windows 10 which includes Group Policy editor. In other words, the script dose not work on Windows 10 Home Edition.

Basically, the script executes following:
- Register scheduler event which is invoked for Security Audit event ID=4800 (Lock) and ID=4801 (Unlock).
- Enable logging of Logon and Logoff related Security Audit event.
