@echo off
setlocal
path C:\ProgramData\chocolatey\bin;%PATH%
find.exe %*
endlocal
