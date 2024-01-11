@echo off
setlocal
path %~dp0;%PATH%
copyDataUrlToClipboard.pyw %*
endlocal
