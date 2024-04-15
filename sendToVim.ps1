$dirs = @()
# Scoop
$dirs += $Env:USERPROFILE + '\scoop\apps\vim\current'
# Chocolatey
$dirs += 'C:\tools\vim'
# My favorite location
$dirs += 'C:\opt\vim'
# Standard location
$dirs += 'C:\Program Files\Vim'
$dirs += 'C:\Program Files (x86)\Vim'
$vimpath = 'C:\Windows'
$ErrorActionPreference = "silentlycontinue"
foreach ($dir in $dirs) {
	if (Test-Path $dir + '\gvim.exe') {
		# The directory has gvim.exe inside.
		$vimpath = $dir
		break
	}
	$dirs = Get-ChildItem -Path $dir -Filter vim* | Sort-Object -Descending
	if ($dirs.Length -gt 1) {
		# The directory has vimXX subfolder.
		$vimpath = $dir + '\' + $dirs[0]
		break
	}
}
$ErrorActionPreference = "continue"

$ENV:PATH = "$vimpath;" + $ENV:PATH

if ($args.Length -eq 0) {
	Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList '--remote-silent .'
} else {
	foreach ($arg in $args) {
		$argumentlist = ' --remote-silent "' + $arg + '"'
		Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList $argumentlist
	}
}
