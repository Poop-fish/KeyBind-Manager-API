import ctypes, threading, time, platform
from collections import defaultdict
#!-------------------- Configuration --------------------

IS_WINDOWS = platform.system() == "Windows"
if IS_WINDOWS:
    user32 = ctypes.windll.user32
    """Windows virtual key codes"""
    VK_CODES = {
        **{chr(i).lower(): i for i in range(0x41, 0x5B)}, # \\ Alphabet keys (lowercase) a-z
        **{str(i): i + 0x30 for i in range(10)}, # \\ Number keys (0-9)
        **{f"f{i}": 0x70 + i - 1 for i in range(1, 25)}, # \\ Function keys (F1-F24)
        
        # ----------Keys----------
        'left_mouse': 0x01,
        'right_mouse': 0x02,
        'middle_mouse': 0x04,
        'ctrl': 0x11, 
        'shift': 0x10, 
        'alt': 0x12,
        'esc': 0x1B, 
        'enter': 0x0D, 
        'tab': 0x09, 
        'space': 0x20,
        'backspace': 0x08, 
        'capslock': 0x14,
        'left': 0x25, 
        'up': 0x26, 
        'right': 0x27,
        'down': 0x28,
        'num_0': 0x60, 
        'num_1': 0x61, 
        'num_2': 0x62, 
        'num_3': 0x63,
        'num_4': 0x64, 
        'num_5': 0x65, 
        'num_6': 0x66, 
        'num_7': 0x67,
        'num_8': 0x68, 
        'num_9': 0x69,
        'volume_up': 0xAF, 
        'volume_down': 0xAE, 
        'volume_mute': 0xAD,
        'win_left': 0x5B,
        'win_right': 0x5C,  
        'media_play_pause': 0xB3,  
        'media_stop': 0xB2, 
        'media_previous': 0xB1,  
        'media_next': 0xB0,  
        'print_screen': 0x2C,  
        'scroll_lock': 0x91,  
        'pause': 0x13, 
        'num_lock': 0x90,  
        'num_divide': 0x6F, 
        'num_multiply': 0x6A,  
        
        # \\ Extended Function keys
        # **{f"f{i}": 0x70 + i - 1 for i in range(25, 45)},  # F25-F44
        
        # \\ Placeholder for additional gamepad or joystick buttons (not implemented directly)
        # 'gamepad_a': 0x0001,  # \\  Example gamepad button
        # 'gamepad_b': 0x0002,  # \\ Example gamepad button
    }
KEYS = VK_CODES

#!-------------------- Core Class --------------------

class KeybindManager:
    def __init__(self):
        self.keybinds = defaultdict(dict)
        self.active = False
        self.listener_thread = None
        self.lock = threading.RLock()  
        self.last_processed = 0

    def register(self, combination, action, cooldown=0.3, press_callback=False):
        keys = tuple(KEYS[k.lower()] for k in combination.split("+") if k.lower() in KEYS)
        with self.lock:
            self.keybinds[keys] = {
                'action': action,
                'cooldown': cooldown,
                'last_trigger': 0,
                'press_callback': press_callback,
                'current_state': False
            }

    def unregister(self, combination):
        keys = tuple(KEYS[k.lower()] for k in combination.split("+") if k.lower() in KEYS)
        with self.lock:
            if keys in self.keybinds:
                del self.keybinds[keys]

    def start(self):
        if not self.active:
            self.active = True
            self.listener_thread = threading.Thread(target=self._monitor_input, daemon=True)
            self.listener_thread.start()

    def stop(self):
        self.active = False
        if self.listener_thread:
            self.listener_thread.join()

    def _monitor_input(self):
        while self.active:
            try:
                current_time = time.time()
                actions_to_trigger = []
                with self.lock:
                    if current_time - self.last_processed < 0.005: # \\ Prevent duplicate processing within 5ms
                        continue
                    self.last_processed = current_time
                    for keys, bind in list(self.keybinds.items()):
                        pressed = all(self._is_pressed(k) for k in keys)
                        if bind['press_callback']:
                            if pressed and not bind['current_state']:
                                if current_time - bind['last_trigger'] >= bind['cooldown']:
                                    actions_to_trigger.append(bind['action'])
                                    bind['last_trigger'] = current_time
                                    bind['current_state'] = True
                            elif not pressed and bind['current_state']:
                                bind['current_state'] = False
                        else:
                            if pressed and current_time - bind['last_trigger'] >= bind['cooldown']:
                                actions_to_trigger.append(bind['action'])
                                bind['last_trigger'] = current_time
                for action in actions_to_trigger:
                    try:
                        action()
                    except Exception as e:
                        print(f"Keybind action error: {e}")
                time.sleep(0.001)
            except Exception as e:
                print(f"Input monitoring error: {e}")

    def _is_pressed(self, key):
        if IS_WINDOWS:
            return user32.GetAsyncKeyState(key) & 0x8000 != 0

#!-------------------- Global Instances --------------------

keybinder = KeybindManager()

#!-------------------- Public API --------------------
def register_hotkey(combination, action, **kwargs):
    keybinder.register(combination, action, **kwargs)

def unregister_hotkey(combination):
    keybinder.unregister(combination)

def start_listening():
    keybinder.start()

def stop_listening():
    keybinder.stop()

start_listening() # \\ Auto-start the listener 
