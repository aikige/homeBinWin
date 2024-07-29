@echo off

if "x%~1"=="x" goto home

set GOPATH=.;%USERPROFILE%;%USERPROFILE%\Documents;%OneDrive%
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
:check_git_root
REM if .git is exist, that is the root folder of repository.
if exist "%DST%\.git" goto found
REM if DST is a root folder (length of DST is 3), finish search.
if "%DST:~3,1%" == "" goto not_found
pushd "%DST%\.."
set DST=%CD%
popd
goto check_git_root

:end
set DST=
title CMD - %CD%
