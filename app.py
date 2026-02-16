import curses
import textwrap
import data_handler
from lines import h_line
from curses import KEY_BACKSPACE, panel
from os import getcwd, listdir
from data_handler import DataHandler
import lines


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

    edit_mode = False

    cursor_y = 0

    title = "Journal logs"

    num_of_rows_to_display = curses.LINES - 7

    edit_file_title = ""

    title_x = int((curses.COLS - len(title)) / 2)

    on_screen_data = open_data_folder()

    dataHan = DataHandler("./journals/")

    to_be_edited = ""

    while True:
        stdscr.erase()
        stdscr.box()
        h_line(stdscr, 2)
        h_line(stdscr, curses.LINES - 3)

        stdscr.addstr(1, title_x, title, curses.A_BOLD)
        stdscr.addstr(curses.LINES - 2, 1, "[q]uit      [a]dd log")

        if not edit_mode:
            for i in range(len(on_screen_data)):
                cur = " "
                a = curses.A_NORMAL
                if i == cursor_y:
                    cur = ">"
                    a = curses.A_BOLD

                stdscr.addstr(3 + i, 2, cur + " " + on_screen_data[i][:-4], a)

        else:
            stdscr.addstr(3, 2, edit_file_title, curses.A_BOLD)
            lines.h_line(stdscr, 4)

            max_width = curses.COLS - 4
            wrapped = textwrap.wrap(to_be_edited, max_width)

            for i, line in enumerate(wrapped):
                stdscr.addstr(5 + i, 2, line)

            # stdscr.addstr(5, 2, to_be_edited, curses.A_BOLD)

        stdscr.refresh()  # ← IMPORTANT
        c = stdscr.getch()  # ← AFTER drawing

        if not edit_mode:
            if c == ord("\n"):
                if on_screen_data:
                    edit_mode = True
                    edit_file_title = on_screen_data[cursor_y]
                    to_be_edited = dataHan.read_file(on_screen_data[cursor_y]) or ""
            elif c == ord("q"):
                break
            elif c == ord("e"):
                popup_input(stdscr, "new file", "> ")
            elif c == ord("j"):
                if on_screen_data:
                    cursor_y = (cursor_y + 1) % len(on_screen_data)
            elif c == ord("k"):
                if on_screen_data:
                    cursor_y = (cursor_y - 1) % len(on_screen_data)
        else:
            if c == 10:  # Enter
                dataHan.write(edit_file_title, to_be_edited)
                edit_mode = False
            elif c in (8, 127, curses.KEY_BACKSPACE):
                to_be_edited = to_be_edited[:-1]
            elif 32 <= c <= 126:  # printable ASCII
                to_be_edited += chr(c)


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
