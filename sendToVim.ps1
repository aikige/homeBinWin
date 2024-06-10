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

# Restore space separated absolute path.
function restore_absolute_path($files) {
	$found_files = @()
	foreach ($file in $files) {
		if (Split-Path $file -IsAbsolute) {
			$found_files += $file
			continue
		} else {
			$found_files[-1] += ' ' + $file
		}
	}
	return $found_files
}

$vimpath = find_vimpath $dirs $vimpath
$ENV:PATH = "$vimpath;" + $ENV:PATH

if ($args.Length -eq 0) {
	Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList '--remote-silent .'
} else {
	if ($args[0] -eq '-a') {
		# For shell:sendto: absolute path reconstruction.
		$null, $args = $args
		$files = restore_absolute_path $args
	} else {
		# Called from command line.
		$files = $args
	}
	foreach ($file in $files) {
		$argumentlist = ' --remote-silent "' + $file + '"'
		Start-Process -NoNewWindow -FilePath 'gvim' -ArgumentList $argumentlist
	}
}
