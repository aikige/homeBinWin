call :createPS1Link GVim.lnk "%~dp0\..\sendToVim.ps1"
call :createLink copyDataUrlToClipboard.lnk "%~dp0\..\copyDataUrlToClipboard.pyw"
exit /b

:createPS1Link
REM 1st parameter: Link name
REM 2nd parameter: Link target script path (relative/absolute)
powershell -File %~dp0\..\createShortcut.ps1 -Minimized "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" powershell.exe -File "%~f2" %3 %4 %5
exit /b

:createLink
REM 1st parameter: Link name
REM 2nd parameter: Link target script path (relative/absolute)
powershell -File %~dp0\..\createShortcut.ps1 -Minimized "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" "%~f2" %3 %4 %5
exit /b
