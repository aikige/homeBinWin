$len = $args.Length
$vimdirs = @()
$vimdirs += 'C:\opt\vim'
$vimdirs += 'C:\tools\vim'
$vimdirs += 'C:\Program Files\Vim'
$vimdirs += 'C:\Program Files (x86)\Vim'
$vimpath = 'C:\Windows'
$ErrorActionPreference = "silentlycontinue"
foreach ($dir in $vimdirs) {
	$dirs = Get-ChildItem -Path $dir -Filter vim* -Recurse
	if ($dirs.Length -gt 1) {
		$vimpath = $dir + '\' + $dirs[0]
		break
	}
}
$ErrorActionPreference = "continue"

$ENV:PATH = "$vimpath;" + $ENV:PATH

if ($len -eq 0) {
	Start-Process -FilePath 'gvim' -ArgumentList '--remote-silent .'
} else {
	foreach ($arg in $args) {
		$argumentlist = '--remote-silent ' + $arg
		Start-Process -FilePath 'gvim' -ArgumentList $argumentlist
	}
}
