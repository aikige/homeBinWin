import os
import re
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', default=os.getcwd())
parser.add_argument('-l', '--file_list', default='depends.txt')
args = parser.parse_args()

# Find '*.d' file.
dep_files = []
for current_dir, sub_dirs, files_list in os.walk(args.directory):
    for file in files_list:
        if re.search(r'\.d$', file):
            dep_files.append(current_dir + os.sep + file)

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
            filenames = re.split(r'\s+', line)
            for filename in filenames:
                filename = filename.replace('%20', r'\ ')
                if re.match('[a-z]:', filename):
                    drive_letter = filename[0]
                    filename = drive_letter.upper() + filename[1:]
                if os.path.isfile(filename):
                    srcs.append(os.path.abspath(filename))
                else:
                    if (len(filename) > 0):
                        print('Not found: ' + filename, file=sys.stderr)

# Create list of source files.
srcs = list(set(srcs))
srcs.sort()
with open(args.file_list, 'w') as f:
    for src in srcs:
        f.write(src + '\n')

# And execute ctags.
result = subprocess.run(['ctags', '-L', args.file_list])
