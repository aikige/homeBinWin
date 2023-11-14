@echo off
setlocal
path %USERPROFILE%\Apps\jgrep;C:\opt\jgrep;%PATH%
start jgrep2.exe %CD%
endlocal
