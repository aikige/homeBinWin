@echo off
for %%f in (%*) do (
	echo kill pid:%%f
	taskkill /pid %%f /f /t
)
