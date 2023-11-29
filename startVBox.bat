@echo off
setlocal
path %VBOX_MSI_INSTALL_PATH%;%PATH%
VBoxManage startvm %* %VBOX_DEFAULT_VM% --type headless
endlocal
