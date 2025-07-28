import curses

#checking size of terminal
def main(stdscr):
    y, x = stdscr.getmaxyx()
    curses.endwin()
    print(f"Your terminal size is: {y} rows x {x} columns")

curses.wrapper(main)