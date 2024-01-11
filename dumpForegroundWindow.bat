@echo off
setlocal
path %USERPROFILE%\bin;%PATH%
set MEMODIR=%USERPROFILE%\Documents\Log
if not exist %MEMODIR% mkdir %MEMODIR%
pushd %MEMODIR%
dumpForegroundWindow.pyw %*
endlocal
