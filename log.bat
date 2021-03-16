@echo off
setlocal

set LOGFILE=%USERPROFILE%\Documents\Log\%date:/=%-Window_Log.md
if %1 == lock (
    echo - Lock %date% %time% >> %LOGFILE%
) else if %1 == unlock (
    echo - Unlock %date% %time% >> %LOGFILE%
)
endlocal
