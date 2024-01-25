import time
import datetime
from win32gui import GetWindowText, GetForegroundWindow

def remove_unsupported_characters(string, encoding = 'cp932'):
    # From string, remove characters which is not supported by specified encoding.
    return string.encode(encoding, errors='ignore').decode(encoding)

def get_active_window_title():
    return GetWindowText(GetForegroundWindow())

def get_log_string(title, message):
    title = remove_unsupported_characters(title)
    if len(title) > 0:
        title = "`%s` " % (title)
    return "* %s %s%s" % (datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'), title, message)

def format_date():
    return datetime.datetime.today().strftime("%Y%m%d")

def get_log_filename(date):
    return date + "-Window_Log.md"

def log_active_window(verbose = False, message = '', prev_title = None, filename = get_log_filename(format_date())):
    title = get_active_window_title()
    if (prev_title == title):
        return title
    out = get_log_string(title, message)
    if verbose:
        print(out)
    with open(filename, "a", encoding="UTF-8", errors="ignore") as f:
        f.write(out + "\n")
    return title

def keep_logging(interval, skip_duplicate, verbose, message):
    """
    check foreground window title and dump it into file.
    output filename is generated from date.

    Parameters
    ----------
    interval : int
        interval of loop, does not loop when interval = 0.
    skip_duplicate : boolean
        select if duplicated title should be logged or not.
        if this value is True, same title is not logged.
    verbose : boolean
        if true, log is shown to standard output also.
    message : string
        addtional message will be added at then end of log.
    """
    while True:
        date_string = format_date()
        log_filename = get_log_filename(date_string)
        prev_title = None
        while date_string == format_date():
            title = log_active_window(verbose, message, prev_title, log_filename)
            if skip_duplicate:
                prev_title = title
            time.sleep(interval)

if __name__ == '__main__':
    import argparse, sys
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keep_logging',
            help='if this argument is set, keep logging',
            action='store_true', default=False)
    parser.add_argument('-i', '--interval',
            help='set interval of logging in seconds. default interval is 120',
            type=int, default=120)
    parser.add_argument('-s', '--skip_duplicate',
            help='if this argument is set, skip logging of duplicated title',
            action='store_true', default=False)
    parser.add_argument('-v', '--verbose',
            action='store_true', default=False,
            help='show log to standard output also')
    parser.add_argument('message', nargs='*', default=[],
            help='addtional message stored with window title')
    args = parser.parse_args()
    if sys.stdout == None:
        # this will happen when script is invoked by pythonw.
        args.verbose = False
    message = ' '.join(args.message)
    if args.keep_logging:
        keep_logging(args.interval, args.skip_duplicate, args.verbose, message);
    else:
        log_active_window(args.verbose, message);
