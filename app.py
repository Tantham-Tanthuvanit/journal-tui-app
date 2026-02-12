import curses
from lines import h_line
from curses import panel
from os import getcwd, listdir
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
        stdscr.erase()

        stdscr.box()

        h_line(stdscr, 2)

        title_x = int((curses.COLS - len(title)) / 2)

        stdscr.addstr(1, title_x, title, curses.A_BOLD)

        h_line(stdscr, curses.LINES - 3)

        stdscr.addstr(curses.LINES - 2, 1, "[q]uit      [a]dd log")

        for i in range(0, len(on_screen_data)):
            cur = " "
            a = curses.A_NORMAL
            if i == cursor_y:
                cur = ">"
                a = curses.A_BOLD

            stdscr.addstr(3 + i, 2, cur + " " + on_screen_data[i][:-4], a)

        dataHan = DataHandler("./journals/")

        c = stdscr.getkey()

        match c:
            case "q":
                break
            case "a":
                filename = popup_input(stdscr, "journal name", "> ")

                if filename == None:
                    pass
                else:
                    dataHan.write(filename, "")

            case "j":
                cursor_y += 1
                if cursor_y > len(on_screen_data) - 1:
                    cursor_y = 0

            case "k":
                cursor_y -= 1
                if cursor_y < 0:
                    cursor_y = len(on_screen_data) - 1

            case _:
                pass

        on_screen_data = open_data_folder()


def open_data_folder():
    data_folder_path = "./journals/"
    return listdir(data_folder_path)


def popup_input(stdscr, title="Input", prompt="> "):
    h, w = 6, 50
    y = (curses.LINES - h) // 2
    x = (curses.COLS - w) // 2

    win = curses.newwin(h, w, y, x)
    pan = panel.new_panel(win)
    pan.top()

    curses.curs_set(1)
    win.keypad(True)

    text = ""

    while True:
        win.clear()
        win.box()

        win.addstr(1, 2, title, curses.A_BOLD)
        win.addstr(3, 2, prompt + text)

        panel.update_panels()
        curses.doupdate()

        key = win.getch()

        if key in (10, 13):
            break
        elif key in (27,):
            text = None
            break
        elif key in (8, 127, curses.KEY_BACKSPACE):
            text = text[:-1]
        elif 32 <= key <= 126:
            text += chr(key)

    pan.hide()
    panel.update_panels()
    curses.doupdate()
    curses.curs_set(0)

    return text


# helps avoid wrong terminal exits and handles all the inits
curses.wrapper(main)
