#listening to mouse
from pynput.mouse import Listener as MouseListener
def writetofile(x,y):
    position = 'Position of current mouse: ({}, {})\n'.format(x, y)
   # print(position, end="")  # Print to console

    # Write position to a file (append mode)
    with open("mouse_log.txt", 'a') as f:
        f.write(position)
   # print('Position of current mouse:({},{})'.format(x,y))
with MouseListener(on_move=writetofile) as l:
    l.join()