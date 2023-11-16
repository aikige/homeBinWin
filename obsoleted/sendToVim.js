//////////////////////////////////////////////////////////////////////
// JScript version of "sendToVim"
//////////////////////////////////////////////////////////////////////
var args = WScript.Arguments;
var sh = new ActiveXObject('WScript.Shell');
var fs = new ActiveXObject('Scripting.FileSystemObject');

function findGvim(fs) {
	var dirs = [
		'C:\\Program Files (x86)\\Vim',
		'C:\\Program Files\\Vim',
		'C:\\tools\\vim',
		'C:\\opt\\Vim'
	];
	var gvim_path = '';
	for (var i; i < dirs.length; i++) {
		if (fs.FolderExists(dirs[i])) {
			// Note: SubFolders is a Collection and
			// requried to be converted into Enumerator to use in for loop.
			for (e = new Enumerator(fs.GetFolder(dirs[i]).SubFolders);
				!e.atEnd(); e.moveNext()) {
				sd = e.item();
				f = sd.Path + '\\gvim.exe';
				if (fs.FileExists(f) && gvim_path < f) {
					gvim_path = f;
				}
			}
		}
	}
	if (gvim_path.length == 0) {
		gvim_path = 'C:\\Windows\\gvim.bat';
	}
	return gvim_path;
}

var gvim = findGvim(fs);

if (args.length == 0) {
	var cmd = '"' + gvim + '" --remote-silent .'  
} else {
	var cmd = '"' + gvim + '" --remote-silent'  
	for (var i = 0; i < args.length; i++) {
		cmd += ' "' + args(i) + '"'
	}
}
sh.Run(cmd);
