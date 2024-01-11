@echo off
setlocal
set MEMODIR=%USERPROFILE%\Documents\Log
if not exist %MEMODIR% mkdir %MEMODIR%
pushd %MEMODIR%
py %~dp0\dumpForegroundWindow.pyw -k -v --interval=600 %*
endlocal
