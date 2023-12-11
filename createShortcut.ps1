$ws =  New-Object -ComObject WScript.Shell
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
$sc = $ws.CreateShortcut($args[0])
$sc.TargetPath = $args[1]
if ($args.Length -gt 2) {
	$str = $args[2..($args.Length -1)]
	$sc.Arguments = "$str"
}
if ($minimize) {
	$sc.WindowStyle = 7
}
$sc.Save()
