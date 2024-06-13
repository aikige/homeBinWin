@echo off
setlocal
rem path C:\opt\jdk\bin;%PATH%
rem set JAVA_HOME=c:\opt\jdk
call :set_plantuml plantuml.jar

if x%PLANTUML% == x (
	echo No plantuml.jar found.
	exit /b
)
if x%~nx1 == x (
	rem start javaw.exe -jar %PLANTUML% -charset UTF-8 -gui -tsvg
	start javaw.exe -jar %PLANTUML% -charset UTF-8 -gui
) else (
	java.exe -jar %PLANTUML% -charset UTF-8 %*
)
endlocal
goto :eof

:set_plantuml
set PLPATH=c:\opt\plantuml;%USERPROFILE%\bin;%USERPROFILE%\scoop\apps\plantuml\current
set PLANTUML=%~$PLPATH:1
exit /b
