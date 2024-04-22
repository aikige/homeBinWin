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

def fine_relative_file(filename, base_dir):
    base_dir = os.path.abspath(base_dir)
    while (len(base_dir) > 3):
        fn_challenge = base_dir + os.sep + filename
        if os.path.isfile(fn_challenge):
            return os.path.normpath(fn_challenge)
        # go up.
        base_dir = os.path.normpath(os.path.join(base_dir, os.pardir))
    print("not found: " + filename, file=sys.stderr)
    return None

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
        dep_dir = os.path.normcase(os.path.dirname(dep_file))
        for line in f:
            # Remove target statement.
            line = re.sub(r'^.*\.[coh]:', '', line)
            # Remove line-continue mark.
            line = re.sub(r'\\$', '', line)
            # Remove spaces in both ends.
            line = line.strip()
            # Escape spaces in path, to make split work.
            line = line.replace(r'\ ', '%20')
            # Get file-list from input.
            filenames = re.split(r'\s+', line)
            for filename in filenames:
                # Restore escaped space.
                filename = filename.replace('%20', r'\ ')
                # Unify case and separator.
                filename = os.path.normcase(filename)
                if len(filename) == 0:
                    continue
                elif os.path.isabs(filename):
                    # Check if file is exist.
                    if not os.path.isfile(filename):
                        print('Not exist: ' + filename, file=sys.stderr)
                        continue
                    filename = os.path.normpath(filename)
                else:
                    filename = fine_relative_file(filename, dep_dir)
                    if filename is None:
                        continue
                srcs.append(filename)

# Create list of source files.
srcs = list(set(srcs))
srcs.sort()
with open(args.file_list, 'w') as f:
    for src in srcs:
        f.write(src + '\n')

# And execute ctags.
result = subprocess.run(['ctags', '-L', args.file_list])
