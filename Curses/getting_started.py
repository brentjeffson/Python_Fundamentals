import curses
import time

stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.addstr(0, 5, "Name: ")
stdscr.refresh()
time.sleep(2)

curses.curs_set(1)
curses.echo()
curses.nocbreak()
stdscr.keypad(False)

curses.endwin()