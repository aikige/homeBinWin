@echo off
setlocal
path %USERPROFILE%\.pyenv\pyenv-win\shims;%USERPROFILE%\.pyenv\pyenv-win\bin;%PATH%
title PYENV - %CD%
cmd /K python --version
title CMD - %CD%
endlocal
