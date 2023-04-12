#!env python3

import datetime
import time

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

print("Hit the ENTER key (or another key of your choice) until eventually a missed keystroke is detected. Aim for at least four keystrokes per second.\n\nHit Ctrl+C to abort.")

last_time = None
while True:
    key = getch()
    if key == '\x03':
        raise KeyboardInterrupt

    current_time = time.time()
    if last_time is not None:
        time_diff = current_time - last_time
        if time_diff > 0.3:
            print(f'{datetime.datetime.fromtimestamp(current_time):%H:%M:%S.%f}: Time difference between key presses: {time_diff:.2f} seconds - did we miss a keystroke?')
    last_time = current_time
