@echo off
setlocal
path %USERPROFILE%\bin;%PATH%
set MEMODIR=%USERPROFILE%\Documents\Memo
if not exist %MEMODIR% mkdir %MEMODIR%
pushd %MEMODIR%
dumpForegroundWindow.py
endlocal
