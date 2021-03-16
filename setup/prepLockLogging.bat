REN Register script to event.
REN Reference: https://superuser.com/questions/615656/
schtasks.exe /create /tn "Unlock Logging" /mo "*[System[Provider[@Name='Microsoft-Windows-Security-Auditing'] and EventID=4801]]" /ec Security /tr "%~dp0\..\log.bat unlock" /sc ONEVENT
schtasks.exe /create /tn "Lock Logging" /mo "*[System[Provider[@Name='Microsoft-Windows-Security-Auditing'] and EventID=4800]]" /ec Security /tr "%~dp0\..\log.bat lock" /sc ONEVENT

REN Configure Audit Policy to enable logging of 4800 and 4801.
REN For auditpol command, please refer https://docs.microsoft.com/windows-server/administration/windows-commands/auditpol-set
REN For GUID for sub-category of Audit Policy, please check https://docs.microsoft.com/openspecs/windows_protocols/ms-gpac/77878370-0712-47cd-997d-b07053429f6d
auditpol /set /subcategory:{0CCE9215-69AE-11D9-BED3-505054503030},{0CCE9216-69AE-11D9-BED3-505054503030} /success:enable /failure:disable



