$scvim = $Env:USERPROFILE + '\scoop\apps\vim\current\gvim.exe'
$dirs = @()
$dirs += 'C:\opt\vim'
$dirs += 'C:\tools\vim'
$dirs += 'C:\Program Files\Vim'
$dirs += 'C:\Program Files (x86)\Vim'
$vimpath = 'C:\Windows'
$ErrorActionPreference = "silentlycontinue"
if (Test-Path $scvim) {
	$vimpath = $Env:USERPROFILE + '\scoop\apps\vim\current'
} else {
	foreach ($dir in $dirs) {
		$dirs = Get-ChildItem -Path $dir -Filter vim* | Sort-Object -Descending
		if ($dirs.Length -gt 1) {
			$vimpath = $dir + '\' + $dirs[0]
			break
		}
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
