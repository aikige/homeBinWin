@echo off
if "%~1" == "" goto check_upgradable

:exec_upgrade
if "%1" == "vim" goto update_vim
choco upgrade -y %*
goto :eof

:update_vim
choco upgrade -y vim --params "/RestartExplorer"
goto :eof

:check_upgradable
choco outdated

