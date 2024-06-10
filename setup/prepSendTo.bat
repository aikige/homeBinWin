call :createPS1Link GVim.lnk ..\sendToVim.ps1 -a
call :createLink copyDataUrlToClipboard.lnk ..\copyDataUrlToClipboard.pyw
exit /b

:createPS1Link
REM 1st parameter: Link name
REM 2nd parameter: Link target script path (relative/absolute)
powershell -File %~dp0\..\createShortcut.ps1 -m "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" powershell -File "%~s2" %3 %4 %5
exit /b

:createLink
REM 1st parameter: Link name
REM 2nd parameter: Link target script path (relative/absolute)
powershell -File %~dp0\..\createShortcut.ps1 -m "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" "%~s2" %3 %4 %5
exit /b
