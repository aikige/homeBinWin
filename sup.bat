@echo off
if "%~1" == "" goto check_upgradable

:exec_upgrade
scoop update %*
goto :eof

:check_upgradable
call scoop update
call scoop status -l

