@echo off
setlocal

set "arg1=%~1"

if "%arg1%" == "" (
    call :check_upgradable
) else if "%arg1%" == "all" (
    call :exec_upgrade_by_name --all
) else if not "%arg1%"=="%arg1:.=%" (
    call :exec_upgrade_by_id %*
) else (
    call :exec_upgrade_by_name %*
)
goto :eof

:exec_upgrade_by_id
echo Upgrade by ID: %*
winget upgrade --id %*
exit /b

:exec_upgrade_by_name
echo Upgrade by Name: %*
winget upgrade %*
exit /b

:check_upgradable
winget list --upgrade-available
exit /b
