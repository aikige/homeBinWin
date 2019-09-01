@echo off

set GOPATH=%HOMEDRIVE%%HOMEPATH%;%HOMEDRIVE%%HOMEPATH%\Documents

if x%~1==x goto home
if not x%~$GOPATH:1==x goto found
goto %1

:home
pushd %HOMEDRIVE%%HOMEPATH%
goto end

:found
pushd %~$GOPATH:1
goto end

:doc
pushd %HOMEDRIVE%%HOMEPATH%\Documents
goto end

:end
set GOPATH=
