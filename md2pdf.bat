@echo off
REM Convert markdown to PDF using marp.exe
REM https://github.com/marp-team/marp-cli
REM Assumption: following files are placed on the directory which includes this script.
REM - marp.css: style sheet.
REM - Background.png: background image.
setlocal
set BG_IMAGE=Background.png
set BG_DIR=%~dp0
if exist %BG_DIR%\%BG_IMAGE% if not exist Background.png mklink /h %BG_IMAGE% %BG_DIR%\%BG_IMAGE% 
marp --allow-local-files --theme %USERPROFILE%\bin\marp.css --pdf %1
endlocal
