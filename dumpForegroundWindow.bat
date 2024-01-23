@echo off
setlocal
if not defined DFW_INTERVAL set DFW_INTERVAL=600
if not defined DFW_LOG_DIR set DFW_LOG_DIR=%USERPROFILE%\Documents\Log
if not exist "%DFW_LOG_DIR%" mkdir "%DFW_LOG_DIR%"
cd "%DFW_LOG_DIR%"
py %~dp0\dumpForegroundWindow.pyw -k -v --interval=%DFW_INTERVAL% %*
endlocal
