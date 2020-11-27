@echo off
if %1 == small goto :xga
if %1 == large goto :full_hd
if %1 == vga goto :vga
if %1 == svga goto :svga
if %1 == wsvga goto :wsvga
if %1 == xga goto :xga
if %1 == fwxga goto :full_wide_xga
if %1 == fhd goto :full_hd
if %1 == full_hd goto :full_hd
echo unknown size %1
pause

:vga
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 640 480
goto :end

:svga
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 800 600
goto :end

:wsvga
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 1024 576
goto :end

:xga
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 1024 768
goto :end

:full_wide_xga
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 1366 768
goto :end

:full_hd
powershell -NoProfile -ExecutionPolicy Unrestricted Set-ScreenResolution.ps1 1920 1080
goto :end

:end
