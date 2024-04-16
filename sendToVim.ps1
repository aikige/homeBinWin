# $dirs is the list of vim install folder, ordered by preference.
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
# Default location
$dirs += 'C:\Windows'

# Select vim from directory list.
function find_vimpath($dirs) {
	foreach ($dir in $dirs) {
		# Check if the directory exists.
		if (!(Test-Path $dir)) {
			continue
		}
		# Check if the directory has gvim.exe inside.
		if (Test-Path ($dir + '\gvim.exe')) {
			return $dir
		}
		# Check if the sub-directory has gvim.exe inside.
		$vimdirs = Get-ChildItem -Path $dir -Filter vim* | Sort-Object -Descending
		foreach ($vimdir in $vimdirs) {
			$vimdir = $dir + '\' + $vimdir
			if (Test-Path ($vimdir + '\gvim.exe')) {
				return $vimdir
			}
		}
	}
	Write-Error -Message "gvim.exe not found" -ErrorAction Stop 
}
$vimpath = find_vimpath $dirs $vimpath

$ENV:PATH = "$vimpath;" + $ENV:PATH

if ($args.Length -eq 0) {
	Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList '--remote-silent .'
} else {
	foreach ($arg in $args) {
		$argumentlist = ' --remote-silent "' + $arg + '"'
		Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList $argumentlist
	}
}
