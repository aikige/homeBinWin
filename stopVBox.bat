@echo off
setlocal
path %VBOX_MSI_INSTALL_PATH%;%PATH%
VBoxManage controlvm %* %VBOX_DEFAULT_VM% savestate
endlocal
