@echo off

if "x%~1"=="x" goto home

set GOPATH=.;%USERPROFILE%;%USERPROFILE%\Documents;%OneDrive%
if exist "%~dp0/_gopath.bat" call "%~dp0/_gopath.bat"
if exist "%CD%/_gopath.bat" call "%CD%/_gopath.bat"
set DST=%~$GOPATH:1
set GOPATH=
if exist "%DST%" goto found

REM check labels
for %%d in ( home back doc pic git_root ) do if "%%d" == "%~1" goto %%d

REM fall through
:not_found
echo not found: %~1
goto end

:found
echo found: %DST%
pushd "%DST%"
goto end

:back
popd
goto end

:home
pushd %USERPROFILE%
goto end

:doc
pushd %USERPROFILE%\Documents
goto end

:pic
pushd %USERPROFILE%\Pictures
goto end

:git_root
set DST=%CD%
for /f "delims=" %%a in ('git rev-parse --show-toplevel') do (
    set DST=%%a
    goto found
)
goto end

:end
set DST=
title CMD - %CD%
