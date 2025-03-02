# Python Keybind Module 

---

This Python module provides a simple way to manage keybinds (keyboard shortcuts) with customizable actions and cooldowns. The `KeybindManager` class allows you to register, unregister, and monitor key combinations for specific actions, which can be executed when the keys are pressed. This module is designed for Windows and uses `ctypes` to interact with the system.

---

## Features
- Register key combinations with customizable actions.
- Handle both one-time presses and continuous key states with cooldown management.
- Thread-based listener to monitor keyboard inputs.
- Easy integration with your existing Python projects.
- Support for common system keys (e.g., `Ctrl`, `Shift`, `Alt`, `Enter`).

---

## Installation
To use this module, simply clone or download it into your project directory and import the relevant functions and classes.

---

## Usage

### Register a Keybind
To register a hotkey, use the `register_hotkey` function. You can specify multiple keys in combination, and the action will be executed when the keys are pressed.

```python
import time
from PyKeyBinder import register_hotkey, start_listening

# Define an action
def example_action():
    print("Hotkey pressed!")

# Register a hotkey (e.g., Ctrl + Shift + A)
register_hotkey("ctrl+shift+a", example_action)

# Start listening for key presses
start_listening()

# Let the listener run
time.sleep(10)  # You can adjust the duration to keep listening for hotkeys.
```

### Unregister a Keybind
If you need to remove a keybind, use the `unregister_hotkey` function with the key combination you wish to remove.

```python
from PyKeyBinder import unregister_hotkey

# Unregister the previous hotkey
unregister_hotkey("ctrl+shift+a")
```

### Start and Stop the Listener
To begin monitoring the keyboard input, use the `start_listening` function. The listener will run in a separate thread, monitoring the keys and triggering actions when keybinds are pressed.

To stop listening and clean up the listener thread, use the `stop_listening` function.

```python
from PyKeyBinder import start_listening, stop_listening

# Start the keybind listener
start_listening()

# Stop the listener after some time
time.sleep(10)
stop_listening()
```

### Keybind Options
- **Cooldown**: Prevents an action from being triggered too frequently. The default is `0.3` seconds.
- **Press Callback**: Set to `True` to have an action triggered only on the key press event (down state). Set to `False` to trigger the action as long as the key is held.

```python
def action_on_key_press():
    print("Key was pressed.")

# Register hotkey with press callback
register_hotkey("ctrl+shift+f", action_on_key_press, press_callback=True)
```

### Supported Keys
The module supports many virtual key codes (e.g., `ctrl`, `alt`, `shift`, `enter`, etc.). You can use standard keys and function keys like `F1-F24`.

Some of the supported keys include:
- `ctrl`, `shift`, `alt`
- `a`, `b`, `c` (Alphabet keys)
- `1`, `2`, `3` (Number keys)
- `f1`, `f2`, `f3` (Function keys)
- `space`, `enter`, `esc`, `tab`, `backspace`
- Mouse buttons: `left_mouse`, `right_mouse`, `middle_mouse`

You can refer to the `VK_CODES` dictionary for a full list of available keys.

## Configuration
This module is preconfigured for Windows, as it uses `ctypes.windll.user32` to monitor key states. If you plan to use this on a different platform, some changes might be needed to adapt the key monitoring logic.

## Example
Here is a complete example that demonstrates registering keybinds, handling key presses, and monitoring for actions:

```python
import time
from PyKeyBinder import register_hotkey, start_listening, stop_listening

# Define actions
def play_pause_action():
    print("Play/Pause pressed.")

def stop_action():
    print("Stop pressed.")

# Register hotkeys
register_hotkey("ctrl+shift+p", play_pause_action)
register_hotkey("ctrl+shift+s", stop_action)

# Start the listener
start_listening()

# Run the program and keep listening
time.sleep(10)

# Unregister hotkeys after use
unregister_hotkey("ctrl+shift+p")
unregister_hotkey("ctrl+shift+s")

# Stop the listener
stop_listening()
```


## License
This module is licensed under the MIT License. See `LICENSE` for more details.

---
