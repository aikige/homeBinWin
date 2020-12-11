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
