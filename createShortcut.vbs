'# Script to create shortcut.
'#
'# Usage:
'#	createShortcut.vbs SRC DST
'# Where:
'#  SRC: Source file for shortcut.
'#  DST: Path of shortcut. DST should end by ".lnk".
'# Reference Used:
'#  http://www.niji.or.jp/home/toru/notes/40.html

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
	If WScript.Arguments.Count >= 2 Then
		.Arguments = WScript.Arguments(2)
	End If
	.Save
End With
