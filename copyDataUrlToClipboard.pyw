import sys, base64, pyperclip, mimetypes
filename = sys.argv[1]
if filename:
    with open(filename, "rb") as f:
        data_url = "data:%s;base64,%s" % (
                mimetypes.guess_type(filename)[0],
                base64.b64encode(f.read()).decode())
        pyperclip.copy(data_url)
