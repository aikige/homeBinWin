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
choco upgrade -y %*
exit /b

:update_vim
choco upgrade -y vim --params "/RestartExplorer"
exit /b

:check_upgradable
choco outdated
exit /b
