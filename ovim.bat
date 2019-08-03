@echo off
setlocal
path %HOMEPATH%\bin;%PATH%
sendToVim.vbs %*
endlocal
