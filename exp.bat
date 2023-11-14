@echo off
setlocal
if "%PROCESSOR_ARCHITECTURE%" equ "x86" (
    set TARGET=%USERPROFILE%\Apps\tablacus\TE32.exe
) else (
    set TARGET=%USERPROFILE%\Apps\tablacus\TE64.exe
)
if exist %TARGET% (
    start %TARGET% %CD%
) else (
    @explorer %CD%
)
endlocal
