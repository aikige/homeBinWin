import datetime
import sys
import os

def get_log_filename():
    return os.path.abspath(
            '%s/Documents/Log/%s-Window_Log.md' % (
                os.path.expanduser('~'), datetime.datetime.now().strftime('%Y%m%d')))

def add_log(string):
    output = '- %s %s' % (datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'), string)
    with open(get_log_filename(), 'a', encoding='UTF-8', errors='ignore') as f:
        f.write(output + "\n")
        f.flush()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        add_log(' '.join(sys.argv[1:]))
