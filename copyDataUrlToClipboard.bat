@echo off
setlocal
path %~dp0;%PATH%
py copyDataUrlToClipboard.pyw %*
endlocal
