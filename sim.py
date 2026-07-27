import time
from pynput import keyboard
from pynput.keyboard import Controller, Key
import pyperclip

controller = Controller()
current_keys = set()
COMBINATION = {keyboard.Key.cmd, keyboard.KeyCode.from_char('b')}

def type_clipboard():
    text = pyperclip.paste()
    if text:
        # 1. Release the modifier keys programmatically just in case
        controller.release(Key.cmd)
        
        # 2. Give the OS a tiny window to register the keys are up
        time.sleep(0.2)
        
        # 3. Type the string
        controller.press(Key.backspace)
        controller.release(Key.backspace)
        controller.press(Key.backspace)
        controller.release(Key.backspace)
        time.sleep(0.1)
        
        controller.type(text)

def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in COMBINATION):
            type_clipboard()

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
