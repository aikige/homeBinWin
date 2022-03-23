'# sendToVim.vbs, script to send file to existing gvim.exe.

Dim sh
Set sh = WScript.CreateObject("WScript.Shell")
Dim fs
Set fs = WScript.CreateObject("Scripting.FileSystemObject")

'# store gvim.exe to be executed
Dim gvim
gvim = FindGvim(fs)

'# assemble command line.
Dim cmd
If WScript.Arguments.Count = 0 Then
	cmd = """" & gvim & """" & " --remote-silent ."
Else
	cmd = """" & gvim & """" & " --remote-silent "
	For Each arg In WScript.Arguments
		cmd = cmd & " """ & arg & """"
	Next
End If

'# execute it.
sh.Run(cmd)

'# function to find gvim.exe path.
Function FindGvim(fs)
	Dim gvim_dirs
	gvim_dirs = Array( _
	"C:\Program Files\Vim", _
	"C:\Program Files (x86)\Vim", _
	"C:\opt\Vim")
	Dim gvim_path
	gvim_path = ""
	For Each d In gvim_dirs
		If fs.FolderExists(d) Then
			Dim gvim_fs
			Set gvim_fs = fs.GetFolder(d)
			For Each s In gvim_fs.SubFolders
				Dim f
				f = s.Path & "\\" & "gvim.exe"
				If fs.FileExists(f) Then
					If StrComp(gvim_path, f) < 0 Then
						gvim_path = f
					End If
				End If
			Next
		End If
	Next
	If gvim_path = "" Then
		gvim_paths = Array( _
		"C:\Windows\gvim.bat")
		For Each f in gvim_paths
			If fs.FileExists(f) Then
				gvim_path = f
				Exit For
			End If
		Next
	End If
	FindGvim = gvim_path
End Function
