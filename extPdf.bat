@echo off

REM need to avoid to execute script on venv.
REM set path and force to use python in the sytem.
path %LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python311;%LOCALAPPDATA%\Programs\Python\Python310;%PATH%

py %~dp0\extPdf.py %*
