@echo off
REM avoid to execute script on venv.
where deactivate.bat > nil 2>&1
if %ERRORLEVEL% equ 0 call deactivate.bat
py %~dp0\extPdf.py %*
