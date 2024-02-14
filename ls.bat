@echo off
where ls.exe > nul
if %ERRORLEVEL% == 0 goto ls

:dir
echo NOTE: replace "ls" with "dir"
@dir %*
goto :eof

:ls
ls.exe %*

