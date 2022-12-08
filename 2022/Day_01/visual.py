import curses
from curses import textpad
import time
# import locale
# locale.setlocale(locale.LC_ALL, '')
# code = locale.getpreferredencoding()

def compute(data=None):
    if data is None:
        data = open("input.txt").read()
    elves = data.split("\n\n")
    return max(sum(map(int, elf.split())) for elf in elves)




screen = curses.initscr()
curses.echo()
curses.cbreak()

while True:
    try:
    
        screen.getch()
        screen.refresh()
    except KeyboardInterrupt:
        break

curses.endwin()


# Elves
#             MAX
#               0
# 1. 1000 -> 1000       0
#              
# 2. 2000 -> 2000    1000       0

# 3. 3000 -> 3000    2000    1000       0   

# 4. 2500 <- 3000    2000    1000       0    

#            3000    2000    1000       0   