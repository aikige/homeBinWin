@echo off
for %%f in (%*) do (
	echo kill %%f
	taskkill /t /f /im %%f
)
