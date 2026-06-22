@echo off
if "%~1" == "" (
    call :check_upgradable
) else if "%~1" == "vim" (
    call :update_vim
) else (
    call :exec_upgrade %*
)
goto :eof

:exec_upgrade
call :exec_choco choco upgrade -y %*
exit /b

:update_vim
call :exec_choco choco upgrade -y vim --params '/RestartExplorer'
exit /b

:check_upgradable
call :exec_choco choco outdated
exit /b

:exec_choco
powershell -NoProfile -Command "& { %* }"
rem $*
exit /b
