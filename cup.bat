@echo off
if "%~1" == "" (
    call :check_upgradable
) else (
    call :exec_upgrade %*
)
goto :eof

:exec_upgrade
if "%1" == "vim" (
    call :update_vim
) else (
    choco upgrade -y %*
)
exit /b

:update_vim
choco upgrade -y vim --params "/RestartExplorer"
exit /b

:check_upgradable
choco outdated
exit /b
