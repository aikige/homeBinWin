@echo off

if "x%~1"=="x" goto home

set DST=%~s1
if exist %DST% goto found

set GOPATH=%HOMEDRIVE%%HOMEPATH%;%HOMEDRIVE%%HOMEPATH%\Documents
set DST=%~s$GOPATH:1
set GOPATH=
if not x%DST%==x goto found

for %%d in ( home back doc memo ) do if "%%d" == "%~1" set DST=%%d
if not x%DST%==x goto %DST%

pushd %~s1
goto end

:home
pushd %HOMEDRIVE%%HOMEPATH%
goto end

:found
pushd %DST%
goto end

:back
popd
goto end

:doc
pushd %HOMEDRIVE%%HOMEPATH%\Documents
goto end

:memo
pushd %HOMEDRIVE%%HOMEPATH%\Documents\Memo
goto end

:end
set DST=
title CMD - %CD%
