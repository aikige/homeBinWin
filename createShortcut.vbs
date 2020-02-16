'# Script to create shortcut.

Set sh = WScript.CreateObject("WScript.Shell")
Set fs =  WScript.CreateObject("Scripting.FileSystemObject")
If WScript.Arguments.Count < 2 Then
	WScript.Echo "Need 2 arguments: SRC DST"
	WScript.Quit
End If
Set src = fs.GetFile(WScript.Arguments(0))
dst = WScript.Arguments(1)
Set shortcut = sh.CreateShortcut(dst)
With shortcut
	.TargetPath = src.Path
	.WorkingDirectory = src.ParentFolder
	.Save
End With
