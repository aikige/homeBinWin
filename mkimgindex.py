import os
import glob
from urllib.parse import quote

class ImageList:
    def __init__(self, filename='01_ImageList.md', ncols=4):
        files = glob.glob("*.jpg")
        files += glob.glob("*.png")
        files += glob.glob("*.svg")
        path = os.getcwd()
        self.markdown_index(path, files, filename, ncols)

    def markdown_index(self, path, files, filename, ncols):
        with open(filename, 'w', encoding='UTF-8', errors='ignore') as f:
            table_head = '|'
            separator = '|'
            f.write("# Index of `%s`\n" % (path))
            for i in range(0, ncols):
                table_head += "%d|" % (i + 1)
                separator += ":--:|"
            f.write(table_head + "\n")
            f.write(separator + "\n")
            idx = 0
            for file in files:
                idx %= ncols 
                if (idx == 0):
                    f.write('|')
                f.write("%s ![%s](%s)|" % (file, file, quote(file)))
                if (idx == ncols - 1):
                    f.write("\n")
                idx += 1

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ncols', default=4)
    parser.add_argument('-o', '--output_file', default='01_ImageList.md')
    args = parser.parse_args()
    icons = ImageList(args.output_file, args.ncols)
