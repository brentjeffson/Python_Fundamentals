import curses
import time

curses.initscr()

def percentage():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    win = curses.newwin(3, 32, 3, 30)
    win.border(0)
    loading = 0
    while loading < 100:
        loading += 1
        time.sleep(0.03)
        update_progress(win, loading)
    win.getch()


def update_progress(win, progress):
    rangex = (30 / float(100)) * progress
    pos = int(rangex)
    display = '-'
    if pos != 0:
        win.attron(curses.color_pair(1))
        win.addstr(1, pos, "{}".format(display))
        win.attroff(curses.color_pair(1))
        win.refresh()

percentage()

curses.endwin()