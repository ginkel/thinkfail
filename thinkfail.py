#!python3

import datetime
import sys
import termios
import time
import tty

def read_single_key():
    """Read a single key from STDIN."""
    # Save the current terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Set the terminal settings to raw mode
        tty.setraw(fd)
        # Read a single key from STDIN
        key = sys.stdin.read(1)
        if key == '\x03':
            raise KeyboardInterrupt
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

last_time = None
while True:
    # read a single character from STDIN
    key = read_single_key()
    sys.stdout.write('\x1b[2K')  # erase the previous line
    sys.stdout.write('\x1b[1G')  # move the cursor to the beginning of the line
    sys.stdout.flush()
    # get the current time
    current_time = time.time()
    # calculate the time difference between the last keypress and the current keypress
    if last_time is not None:
        time_diff = current_time - last_time
        if time_diff > 0.3:
            print(f'{datetime.datetime.fromtimestamp(current_time):%H:%M:%S.%f}: Time difference between key presses: {time_diff:.2f} seconds - did we miss a keystroke?')
    last_time = current_time
