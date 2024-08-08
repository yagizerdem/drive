import curses
import time
import random
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
flag = True

map = []

position = {
    'x':9,
    'y':30
}

cap = random.randint(-8, 8)
cap = 0
direction = 0
left = 20 + cap 
right = 40 +cap

def init():
    for i in range(0,10):
        row = []
        for j in range(0,70):
            if j >= 20 and j < 40:
                row.append(" ")
            else:
                row.append(".")
        map.append(row)

init()

def clear_input_buffer(stdscr):
    # Check if there are any characters in the buffer
    while stdscr.getch() != -1:
        pass  # Discard all characters

def print_map(stdscr):
    stdscr.clear()
    for i in range(0,len(map)):
        for j in  range(len(map[0])):
            stdscr.addstr(i,j, map[i][j] ,  curses.A_BOLD)
    stdscr.refresh()


def update_map():
    map.pop()
    newRow = []
    for j in range(0,70):
        if j >= left + direction and j < right + direction:
            newRow.append(" ")
        else:
            newRow.append(".")
    map.insert(0,newRow)


def main(stdscr):
    curses.curs_set(1)  # Hide the cursor
    stdscr.nodelay(True)
    global flag
    global cap
    global direction
    global left
    global right
    while flag:
        stdscr.clear()
        print_map(stdscr)
        stdscr.addstr(position['x'], position['y'], '^', curses.A_BOLD)
        # Non-blocking getkey, so it doesn't hang if no key is pressed
       
       
        # check collison 
        if(map[position['x']][position['y']] != " "):
            flag = False


        try:
            key = stdscr.getkey()
            if key:
                if key ==  'a':
                    position['y'] -= 1
                elif key ==  'd':
                    position['y'] += 1
        except curses.error:
            # Handle case where no key is pressed (no key to read)
            pass
        finally:
            stdscr.refresh()
            update_map()
            direction += -1 if cap < 0 else 1
            if (cap == 0): direction = 0
            if direction == cap:
                left += cap 
                right += cap
                while(True):
                    cap = random.randint(-8, 8)
                    if(left + cap < 1 or right + cap > 69): continue
                    else: 
                        break
                direction = 0

            clear_input_buffer(stdscr) 
            time.sleep(0.1)



print("game over")


curses.wrapper(main)