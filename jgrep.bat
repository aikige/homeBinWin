@echo off
setlocal
path %USERPROFILE%\Apps\jgrep;C:\opt\jgrep;%PATH%
jgrep2.exe %CD%
endlocal
