@echo off
setlocal
if "%LOG_DST%" == "" set LOG_DST=%USERPROFILE%\Documents\timestamp.log
if not exist "%LOG_DST%" echo Start > "%LOG_DST%"
echo %DATE% %TIME% %* >> "%LOG_DST%"
endlocal
