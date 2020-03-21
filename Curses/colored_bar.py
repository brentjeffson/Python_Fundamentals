import curses

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(" "*100)
    stdscr.attroff(curses.color_pair(1))
    
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(0, 100//2 - 3//2, "100%")
    stdscr.attroff(curses.color_pair(2))

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)