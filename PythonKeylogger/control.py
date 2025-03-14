#controlling keyboard
from pynput.keyboard import Controller as KeyboardController
def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("i am awesome")

controlKeyboard()
#listening to mouse
#listening to keyboard(keylogger)