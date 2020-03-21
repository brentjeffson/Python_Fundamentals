import curses
import time

def main(stdscr):
    curses.curs_set(0)

    while 1:
        key = stdscr.getch()

        stdscr.clear()
        if key == curses.KEY_UP:
            stdscr.addstr(0, 0, "Going Up")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0, 0, "Going Down")
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "Submitting")
        else:
            stdscr.addstr(0, 0, "Invalid Key")

        stdscr.refresh()

curses.wrapper(main)