@echo off
REM Convert markdown to PDF using marp.exe
REM https://github.com/marp-team/marp-cli
REM Assumption: following files are placed on the directory which includes this script.
REM - marp.css / marp-doc.css: style sheet.
REM - Background.png: background image.
setlocal
set BG_IMAGE=Background.png
set WORK_DIR=%~dp0
set FORMAT=--pdf

REM select layout
if x%1 == x-doc (
	set CSS=marp-doc.css
	shift
) else (
	set CSS=marp.css
)

REM watch option
if x%1 == x-w (
	set WATCH=-w
    set FORMAT=--html
	shift
)

set MDFILES=%*

if not exist %CSS% if exist %WORK_DIR%\%CSS% mklink /h %CSS% %WORK_DIR%\%CSS%
if not exist %BG_IMAGE% if exist %WORK_DIR%\%BG_IMAGE% mklink /h %BG_IMAGE% %WORK_DIR%\%BG_IMAGE% 

marp --allow-local-files %WATCH% --html --theme %CSS% %FORMAT% %MDFILES%
endlocal
