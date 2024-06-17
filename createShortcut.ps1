<#
.SYNOPSIS
createShortcut.ps1 [-Minimized] <LinkName> <TargetProgram> [<Args> ...]

.DESCRIPTION
Creates a link for the specified program.

.PARAMETER Minimized
A switch to minimize the Window invoked from the shortcut.
This switch shall be placed as 1st argument.
.PARAMETER LinkName
1st positional parameter that specifies name of the link.
.PARAMETER TargetProgram
2nd positional parameter that specifies target file to be linked.
.PARAMETER Args
List of arguments that is passed to shortcut as Arguments.
Multiple arguments can be specified.

.NOTE
This script does not follow standard parameter manner in PowerShell and
`Get-Help` for this script will not work as expected.
#>
if (($args.Length -gt 0) -and ($args[0] -eq '-Minimized')) {
	$minimize = $true
	$null, $args = $args	# Shift args.
} else {
	$minimize = $false
}
if ($args.Length -lt 2) {
	echo "Need 2 arguments: [-Minimized] <LinkName> <TargetProgram> [<Args> ...]"
	exit
}
$link_name = $args[0]
$target_program = $args[1]
$null, $null, $args = $args
echo $link_name
echo $target_program
$ws =  New-Object -ComObject WScript.Shell
$sc = $ws.CreateShortcut($link_name)
$sc.TargetPath = $target_program
if ($args.Length -gt 0) {
	$sc.Arguments = "$args"
}
if ($minimize) {
	$sc.WindowStyle = 7
}
$sc.Save()
