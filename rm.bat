@echo off
setlocal
where rm.exe > nul
if %ERRORLEVEL% == 0 goto rm

call :find bash.exe
if not x%BASH%==x goto bash

:del
REM if no rm.exe found, use del command instead.
echo execute "del %*"
del %*
goto end

:bash
echo execute "rm %*" on %BASH%
%BASH% -c "rm %*"
endlocal
goto end

:rm
rm.exe %*
goto end

:find
set BASHPATH=%ProgramFiles%\git\bin;%ProgramFiles%\git\usr\bin;%PATH%
set BASH=%~s$BASHPATH:1
exit /b

:end
endlocal
