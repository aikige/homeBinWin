$NewPath = Resolve-Path($args[0])
echo "== New Item =="
[string]$NewPath

$PathStr = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$PathArray = $PathStr.Split(";")
$PathStr = [System.Environment]::GetEnvironmentVariable("PATH", "User")
$PathArray += $PathStr.Split(";")
$UserPathArray = $PathStr.Split(";")
echo "== Current Path =="
$PathArray
foreach ( $PathEntry in $PathArray ) {
	if ( $PathEntry -eq $NewPath ) {
		echo "Already Exist"
		exit
	}
}
$UserPathArray += $NewPath
$PathStr = $UserPathArray -join ';'
echo "== Updated Path =="
$PathStr

[System.Environment]::SetEnvironmentVariable("PATH", $PathStr, "User")
