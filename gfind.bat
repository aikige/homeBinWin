@echo off
setlocal
path C:\ProgramData\chocolatey\bin;C:\ProgramData\chocoportable\bin;%PATH%
find.exe %*
endlocal
