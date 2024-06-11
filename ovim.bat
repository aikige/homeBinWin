@echo off
powershell -File "%~dp0\sendToVim.ps1" %*
REM Following style closes Command Prompt and not suitable for the purpose.
rem powershell -WindowStyle Hidden -F "%~dp0\sendToVim.ps1" %*
REM Reference: https://arimasou16.com/blog/2018/12/06/00281/
REM Reference: https://letspowershell.blogspot.com/2016/03/powershell.html
rem "%~dp0\sendToVim.js" %*
rem "%~dp0\sendToVim.vbs" %*
