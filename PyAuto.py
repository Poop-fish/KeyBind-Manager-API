# Python module that allows you to programmatically control the mouse and keyboard. It is commonly used for
# Automating GUI interactions (e.g., clicking, typing, dragging).

import ctypes

class WinMouse:
    def click(self):
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # \\ Mouse down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # \\ Mouse up

class AutoFunc:
    def __init__(self):
        self.mouse = WinMouse()
    
    def click(self):
        self.mouse.click()
