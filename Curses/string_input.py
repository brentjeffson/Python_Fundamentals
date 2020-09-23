import curses
from curses import textpad



def main(stdscr):
    win = curses.newwin(6, 23, 4, 1)
    pad = textpad.rectangle(stdscr, 3, 0, 10, 24)
    stdscr.refresh()
    win.addstr("Pre-Inputted Data")
    box = textpad.Textbox(win, insert_mode=False)
    
    box.edit()
    contents = box.gather().strip()
    
    stdscr.clear()

    stdscr.addstr(repr(contents))
    stdscr.getch()

curses.wrapper(main)