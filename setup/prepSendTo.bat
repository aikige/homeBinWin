call :createPS1Link GVim.lnk ..\sendToVim.ps1 -a
exit /b

:createPS1Link
powershell -file ..\createShortcut.ps1 -m "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\SendTo\%1" powershell "%~df2"
exit /b
