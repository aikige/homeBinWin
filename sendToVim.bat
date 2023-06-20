@echo off
set GVIM_EXE=C:\Windows\gvim.bat
for /d %%d in (
"C:\Program Files\ (x86)\Vim\vim*"
"C:\Program Files\Vim\vim*"
"C:\tools\vim\vim*"
"C:\opt\vim\vim*"
) do (
    if exist "%%d\gvim.exe" set GVIM_EXE="%%d\gvim.exe"
)
if not exist %GVIM_EXE% (
    echo "Not exist"
    goto :eof
)
if "x%1" == "x" (
    %GVIM_EXE% --remote-silent
) else (
    %GVIM_EXE% --remote-silent %*
)
