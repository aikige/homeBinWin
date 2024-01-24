@echo off
if "%~1" == "" goto check_upgradable

:exec_upgrade
choco upgrade -y %*
goto :eof

:check_upgradable
choco outdated

