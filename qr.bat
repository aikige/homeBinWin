@echo off
setlocal
for /f "usebackq delims=" %%t in (`py -c "import os, sys; print(os.path.dirname(sys.executable))"`) do set TARGETDIR=%%t
set SCRIPT=%TARGETDIR%\lib\site-packages\qrcode\console_scripts.py
if exist %SCRIPT% call :exec_qr %*
endlocal
goto :eof

:exec_qr
rem path %TARGETDIR%;%PATH%
rem python.exe %SCRIPT% %*
rem %TARGETDIR%\python.exe %SCRIPT% %*
py %SCRIPT% %*
exit /b
