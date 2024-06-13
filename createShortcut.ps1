if ($args.Length -lt 2) {
	echo "Need 2 arguments: LINK_NAME TARGET_PROGRAM ARGS"
	exit
}
if ($args[0] -eq '-m') {
	$minimize = $true
	$null, $args = $args	# Shift args.
} else {
	$minimize = $false
}
$ws =  New-Object -ComObject WScript.Shell
$sc = $ws.CreateShortcut($args[0])
$sc.TargetPath = $args[1]
if ($args.Length -gt 2) {
	$null, $null, $args = $args
	$sc.Arguments = "$args"
}
if ($minimize) {
	$sc.WindowStyle = 7
}
$sc.Save()
