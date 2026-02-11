import curses
from os import getcwd, listdir
import re
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

    on_screen_data = open_data_folder()

    while True:
        title_x = int((curses.COLS - len(title)) / 2)

        stdscr.hline(0, 0, curses.ACS_HLINE, curses.COLS)
        stdscr.addstr(1, title_x, title, curses.A_BOLD)
        stdscr.hline(2, 0, curses.ACS_HLINE, curses.COLS)

        stdscr.hline(curses.LINES - 1, 0, curses.ACS_HLINE, curses.COLS)

        stdscr.hline(curses.LINES - 3, 0, curses.ACS_HLINE, curses.COLS - 1)

        stdscr.addstr(curses.LINES - 2, 1, "[q]uit      [a]dd log")

        stdscr.vline(0, 0, curses.ACS_VLINE, curses.LINES)
        stdscr.vline(0, curses.COLS - 1, curses.ACS_VLINE, curses.LINES)

        for i in range(0, len(on_screen_data)):
            stdscr.addstr(3 + i, 3, on_screen_data[i][:-4])

        dataHan = DataHandler("./journals/")

        c = stdscr.getkey()

        match c:
            case "q":
                break
            case "a":
                filename = ""

                while True:
                    key = stdscr.getch()

                    if key == 10:  # error
                        break
                    elif key in (8, 127):
                        filename = filename[:-1]
                    elif 32 <= key <= 126:
                        filename += chr(key)

                filename = re.sub(r'[<>:"/\\|?*\n]', "", filename)

                dataHan.write(filename, "")

            case _:
                pass

        on_screen_data = open_data_folder()


def open_data_folder():
    data_folder_path = "./journals/"
    return listdir(data_folder_path)


# helps avoid wrong terminal exits and handles all the inits
curses.wrapper(main)
