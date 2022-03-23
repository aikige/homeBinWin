echo "== Argument =="
[string]$args

$NewPath = Resolve-Path([string]$args)
echo "== New Item =="
[string]$NewPath

<#
Reference:
https://docs.microsoft.com/ja-jp/dotnet/api/system.environment.getenvironmentvariable
https://docs.microsoft.com/ja-jp/dotnet/api/system.environment.setenvironmentvariable
#>
$PathStr = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$PathArray = $PathStr.Split(";") -ne ""
$PathStr = [System.Environment]::GetEnvironmentVariable("PATH", "User")
$UserPathArray = $PathStr.Split(";") -ne ""
$PathArray += $UserPathArray
echo "== Current Path =="
$PathArray

foreach ( $PathEntry in $PathArray ) {
	if ( $PathEntry -eq $NewPath ) {
		echo "== Already Exist =="
		exit
	}
}

$UserPathArray += $NewPath
$PathStr = $UserPathArray -join ';'
echo "== Updated Path =="
$PathStr

[System.Environment]::SetEnvironmentVariable("PATH", $PathStr, "User")
