import curses


def h_line(stdscr, y):
    stdscr.hline(y, 1, curses.ACS_HLINE, curses.COLS - 2)
    stdscr.addch(y, 0, curses.ACS_LTEE)
    stdscr.addch(y, curses.COLS - 1, curses.ACS_RTEE)
