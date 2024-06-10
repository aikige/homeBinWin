call :createPS1Link GVim.lnk ..\sendToVim.ps1 -a
exit /b

:createPS1Link
powershell -File %~dp0\..\createShortcut.ps1 -m "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" powershell -File "%~s2" %3 %4 %5
exit /b
