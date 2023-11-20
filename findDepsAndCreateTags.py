import os
import re
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('root', nargs='?', default=os.getcwd(),
                    help='root of dependecy file, used to convert relative path to absolute path.')
parser.add_argument('-l', '--file_list', default='depends.txt',
                    help='name of file-list passed to ctags.')
args = parser.parse_args()

# Find '*.d' file.
root = os.path.abspath(args.root)
dep_files = []
for current_dir, sub_dirs, files_list in os.walk(root):
    for filename in files_list:
        if re.search(r'\.d$', filename):
            dep_files.append(current_dir + os.sep + filename)

# Get list of sources from dependency file.
srcs = []
for dep_file in dep_files:
    with open(dep_file) as f:
        for line in f:
            # Remove target statement.
            line = re.sub(r'^.*\.[coh]:', '', line)
            # Remove line-continue mark.
            line = re.sub(r'\\$', '', line)
            line = line.strip()
            # Replace space escape to make split works.
            line = line.replace(r'\ ', '%20')
            # Unify path separator.
            for sep in ['\\', '/']:
                if (sep != os.sep):
                    line = line.replace(sep, os.sep) 
            filenames = re.split(r'\s+', line)
            for filename in filenames:
                filename = filename.replace('%20', r'\ ')
                if re.match('^[a-z]:', filename):
                    drive_letter = filename[0]
                    filename = drive_letter.upper() + filename[1:]
                elif len(filename) > 0 \
                and not re.match(r'^[\\\/]', filename) \
                and not re.match('^[A-Z]:', filename):
                    filename = root + os.sep + filename
                if os.path.isfile(filename):
                    srcs.append(os.path.abspath(filename))
                elif (len(filename) > 0):
                    print('Not found: ' + filename, file=sys.stderr)

# Create list of source files.
srcs = list(set(srcs))
srcs.sort()
with open(args.file_list, 'w') as f:
    for src in srcs:
        f.write(src + '\n')

# And execute ctags.
result = subprocess.run(['ctags', '-L', args.file_list])
