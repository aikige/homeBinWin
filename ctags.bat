@echo off
setlocal
path C:\opt\ctags;%PATH%
ctags.exe %*
endlocal
