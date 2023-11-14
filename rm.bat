@echo off
setlocal
call :find bash.exe
if x%BASH%==x (
    del %*
) else (
    echo execute "rm %*" on %BASH%
    %BASH% -c "rm %*"
)
endlocal
goto :eof

:find
set BASHPATH=%ProgramFiles%\git\bin;%ProgramFiles%\git\usr\bin
set BASH=%~s$BASHPATH:1
exit /b
