import time
import datetime
from win32gui import GetWindowText, GetForegroundWindow

def get_active_window_title():
    return GetWindowText(GetForegroundWindow())

def get_log_string(title):
    return datetime.datetime.now().strftime('* %Y%m%d-%H:%M:%S `') + title + '`'

def format_date(date):
    return date.strftime("%Y%m%d")

def get_log_filename(date):
    return date + "-Window_Log.md"

def log_active_window(interval):
    day = format_date(datetime.datetime.today())
    old = ""
    with open(get_log_filename(day), "a", encoding="UTF-8", errors="ignore") as f:
        while day == format_date(datetime.datetime.now()):
            title = get_active_window_title()
            if (title != old):
                out = get_log_string(title)
                print(out)
                f.write(out + "\n")
                f.flush()
                time.sleep(interval)
                old = title

def keep_logging(interval):
    while True:
        log_active_window(interval)

if __name__ == '__main__':
    keep_logging(60)
