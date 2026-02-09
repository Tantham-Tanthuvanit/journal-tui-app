import curses


# main program
def main(stdscr):
    # clear screen
    stdscr.clear()

    for i in range(0, 11):
        v = i - 10
        stdscr.addstr(i, 0, "10 divided by {} is {}".format(v, 10 / v))

        stdscr.refresh()
        stdscr.getkey()


# helps avoid wrong terminal exits and handles all the inits
curses.wrapper(main)
