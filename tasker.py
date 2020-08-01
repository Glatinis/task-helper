import pyautogui
import pynput
from pynput.mouse import Listener

def click(x, y):
    pyautogui.click(x, y)

def getPos():
    return pyautogui.position()

def onNextClick():
    with Listener(on_click=onClick) as listener:
        listener.join()
    return True

def onClick(x, y, button, pressed):
    return False
