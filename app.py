import curses
from data_handler import DataHandler


# main program
def main(stdscr):
    # coordinates are passed in as y and then x, top left is (0,0)
    # can determine the size of screen by using curses.LINES and curses.COLS
    # legal coordinates are (0,0) to (LINES-1, COLS-1)
    # must always call refresh() to update

    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.start_color()  # anble color text
    curses.curs_set(0)

    cursor_x = 0
    cursor_y = 0

    title = "Journal logs"

    title_x = int((curses.COLS - len(title)) / 2)

    while True:
        stdscr.hline(0, 0, curses.ACS_HLINE, curses.COLS)
        stdscr.addstr(1, title_x, title, curses.A_BOLD)
        stdscr.hline(2, 0, curses.ACS_HLINE, curses.COLS)

        stdscr.hline(curses.LINES - 1, 0, curses.ACS_HLINE, curses.COLS)

        stdscr.vline(0, 0, curses.ACS_VLINE, curses.LINES)
        stdscr.vline(0, curses.COLS - 1, curses.ACS_VLINE, curses.LINES)

        c = stdscr.getkey()

        match c:
            case "q":
                break
            case _:
                pass


# helps avoid wrong terminal exits and handles all the inits
curses.wrapper(main)
