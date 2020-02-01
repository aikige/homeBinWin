@echo off
setlocal
path %~dp0;%PATH%
sendToVim.vbs %*
endlocal
