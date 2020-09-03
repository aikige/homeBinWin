@echo off
setlocal
path C:\opt\jdk\bin;%PATH%
set JAVA_HOME=c:\opt\jdk
call :set_plantuml plantuml.jar

if x%PLANTUML% == x exit /b
if x%~nx1 == x (
	start javaw.exe -jar %PLANTUML% -charset UTF-8 -gui
) else (
	java.exe -jar %PLANTUML% -charset UTF-8 %*
)
endlocal
goto :eof

:set_plantuml
set PLPATH=c:\opt\plantuml;%USERPROFILE%\bin
set PLANTUML=%~$PLPATH:1
exit /b
