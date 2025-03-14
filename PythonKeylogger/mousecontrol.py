#controlling mouse
from pynput.mouse import Controller as MouseController

#left to right, top to bottom
#from top-left is 0,0

def controlMouse():
    mouse = MouseController()
    mouse.position = (100, 20)
controlMouse()