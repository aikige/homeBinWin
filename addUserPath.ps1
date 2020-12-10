$NewPath = Resolve-Path($args[0])
echo "== New Item =="
[string]$NewPath

<#
Reference:
https://docs.microsoft.com/ja-jp/dotnet/api/system.environment.getenvironmentvariable
https://docs.microsoft.com/ja-jp/dotnet/api/system.environment.setenvironmentvariable
#>
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
