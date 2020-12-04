import time
import datetime
import re
from win32gui import GetWindowText, GetForegroundWindow

def get_active_window_title():
    return GetWindowText(GetForegroundWindow())

def get_log_string(title):
    # replace unusual spaces to normal space.
    title = re.sub('[\u2000-\u200d]', ' ', title)
    return "* %s `%s`" % (datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S'), title)

def format_date(date):
    return date.strftime("%Y%m%d")

def get_log_filename(date):
    return date + "-Window_Log.md"

def log_active_window(interval, skip_duplicate):
    """
    check foreground window title and dump it into file.
    output filename is generated from date.

    Parameters
    ----------
    interval : int
        interval of logging, in seconds.
    skip_duplicate : boolean
        select if duplicated title should be logged or not.
        if this value is True, same title is not logged.
    """
    day = format_date(datetime.datetime.today())
    old = ""
    with open(get_log_filename(day), "a", encoding="UTF-8", errors="ignore") as f:
        while day == format_date(datetime.datetime.now()):
            title = get_active_window_title()
            if (skip_duplicate == True and title == old):
                continue
            out = get_log_string(title)
            print(out)
            f.write(out + "\n")
            f.flush()
            time.sleep(interval)
            old = title

def keep_logging(interval, skip_duplicate):
    while True:
        log_active_window(interval, skip_duplicate)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval',
            help='set interval of logging in seconds. default interval is 120',
            type=int,
            default=120)
    parser.add_argument('-s', '--skip_duplicate',
            help='if this argument is set, skip logging of duplicated title',
            action='store_true',
            default=False)
    args = parser.parse_args()
    keep_logging(args.interval, args.skip_duplicate);
