# Reference: https://stackoverflow.com/questions/54310513/scripted-method-to-find-and-kill-process-using-a-specific-dll
if ($args.Length -eq 0) {
	echo "Argument is required"
	exit
}
foreach ($arg in $args) {
	write-host "Checking DLL $arg..."
	foreach ($p in Get-Process)
	{
		#echo "Checking process $p..."
		foreach ($m in $p.modules)
		{
			if ( $m.FileName -match $arg)
			{
				write-host "Found:" $m.FileName "in" $p.Name "ID:" $p.id
			}
		}
	}
}
