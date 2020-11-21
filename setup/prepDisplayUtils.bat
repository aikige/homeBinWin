setlocal
set UTILITY=%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Utilities
if not exist "%UTILITY%" mkdir "%UTILITY%"
..\createShortcut.vbs ..\set_screen_resolution.bat "%UTILITY%\VGA.lnk" "vga"
..\createShortcut.vbs ..\set_screen_resolution.bat "%UTILITY%\SVGA.lnk" "svga"
..\createShortcut.vbs ..\set_screen_resolution.bat "%UTILITY%\XGA.lnk" "xga"
..\createShortcut.vbs ..\set_screen_resolution.bat "%UTILITY%\Full HD.lnk" "fhd"
..\createShortcut.vbs "%SYSTEMROOT%\system32\DisplaySwitch.exe" "%UTILITY%\Display Clone.lnk" "/clone"
..\createShortcut.vbs "%SYSTEMROOT%\system32\DisplaySwitch.exe" "%UTILITY%\Display Extend.lnk" "/extend"
endlocal
