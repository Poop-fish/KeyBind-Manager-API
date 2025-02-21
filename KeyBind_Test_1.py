import threading
import time
from queue import Queue
from PyKeyBinderAPI.KeyBinder import register_hotkey, unregister_hotkey, start_listening, stop_listening
from PyKeyBinderAPI.PyAuto import AutoFunc, WinMouse

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.click_speed = 0.1
        self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
        self.click_thread.start()
        self.autogui = AutoFunc()
        
        # \\ Register key binds
        
        # register_hotkey("ctrl+q", self.toggle_clicking, press_callback=True)
        register_hotkey("1", self.toggle_clicking, press_callback=True)
        register_hotkey("2", lambda: self.adjust_speed(0.9), press_callback=True)
        register_hotkey("3", lambda: self.adjust_speed(1.1), press_callback=True)

    def toggle_clicking(self):
        self.clicking = not self.clicking
        print(f"Status: {'Running' if self.clicking else 'Stopped'}")

    def adjust_speed(self, factor):
        self.click_speed = max(0.01, min(5.0, self.click_speed * factor))
        print(f"New speed: {self.click_speed:.2f}s")

    def click_loop(self):
        while True:
            if self.clicking:
                self.autogui.click() #! \\ Custom module
            time.sleep(self.click_speed)

if __name__ == "__main__":
    clicker = AutoClicker()
    start_listening()
    while True:
        time.sleep(1) 




