@echo off
if "%~1" == "" (
    call :check_upgradable
) else if "%~1" == "clean" (
    call :handle_cleanup
) else if "%~1" == "cleanup" (
    call :handle_cleanup
) else if "%~1" == "all" (
    call :handle_upgrade *
) else (
    call :handle_upgrade %*
)
goto :eof

:handle_cleanup
call scoop cleanup
exit /b

:handle_upgrade
call scoop update %*
exit /b

:check_upgradable
call scoop update
call scoop status -l
exit /b

