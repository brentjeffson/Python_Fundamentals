import curses
import time

def main(stdscr):
    stdscr.addstr(1, 5, "Using Wraper")
    stdscr.refresh()
    time.sleep(2)

curses.wrapper(main)