@echo off
setlocal
path %~dp0;%PATH%
py %~dp0\findDepsAndCreateTags.py %*
endlocal
