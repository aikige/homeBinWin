@echo off
setlocal
path %USERPROFILE%\bin;%PATH%
copyDataUrlToClipboard.pyw %*
endlocal
