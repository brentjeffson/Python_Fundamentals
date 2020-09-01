import curses

menus = ["Novel", "Chapters", "Settings", "Exit"]

def printMenu(stdscr, selectedRow):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for idx, menu in enumerate(menus):
        x = width // 2 - len(menu) // 2
        y = height // 2 - len(menus) // 2 + idx

        if selectedRow == idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, menu)
            stdscr.attroff(curses.color_pair(1))
        else: 
            stdscr.addstr(y, x, menu)
        


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)

    selectedRow = 0
    printMenu(stdscr, selectedRow)
    while True:
        # stdscr.addstr(0, 0, f"ROW: {selectedRow}")        
        selectorKey = stdscr.getch()
        stdscr.addstr(0, 0, str(selectorKey)) 
        stdscr.getch()       

        if selectorKey == curses.KEY_UP and selectedRow > 0:
            selectedRow -= 1
        elif selectorKey == curses.KEY_DOWN and selectedRow < len(menus) - 1: 
            selectedRow += 1
        elif selectedRow == curses.KEY_ENTER or selectorKey in [10, 13]:
            if selectedRow == len(menus) - 1:
                break
            else:
                stdscr.clear()
                stdscr.addstr(f"You Selected {menus[selectedRow]}")
                stdscr.getch()
                printMenu(stdscr, selectedRow)

        printMenu(stdscr, selectedRow)
        
curses.wrapper(main)


