import curses
from curses import textpad



def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)

    textpad.rectangle(stdscr, 0, 0, 2, 24)

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(1, 1, ' '*23)
    stdscr.attroff(curses.color_pair(1))

    height, width = stdscr.getmaxyx()
    win = curses.newwin(1, 10, 4, 0)
    

    stdscr.getch()

curses.wrapper(main)