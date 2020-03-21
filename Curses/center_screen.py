import time
import curses

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    text = "Hello, World"
    h, w = stdscr.getmaxyx()

    y = h // 2
    x = w // 2 - len(text) // 2
    
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, text)
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()
    time.sleep(2)

curses.wrapper(main)