'# sendToVim.vbs, script to send file to existing gvim.exe.

Dim sh
Set sh = WScript.CreateObject("WScript.Shell")
Dim fs
Set fs = WScript.CreateObject("Scripting.FileSystemObject")

'# store gvim.exe to be executed
Dim gvim

'# possible list of gvim.exe
Dim gvims
gvims = Array( _
"C:\Program Files (x86)\Vim\vim81\gvim.exe", _
"C:\Program Files (x86)\Vim\vim80\gvim.exe")

'# select gvim.exe
For Each file In gvims
	If fs.FileExists(file) Then
		gvim = file
		Exit For
	End If
Next

'# assemble command line.
Dim cmd
If WScript.Arguments.Count = 0 Then
	cmd = """" & gvim & """" & " --remote-silent ."
Else
	cmd = """" & gvim & """" & " --remote-silent "
	For Each arg In WScript.Arguments
		cmd = cmd & " " & arg
	Next
End If

'# execute it.
sh.Run(cmd)
