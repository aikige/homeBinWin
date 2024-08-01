param($filename)
$full_path = Convert-Path $filename
echo $full_path | Set-Clipboard
