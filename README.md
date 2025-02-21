# KeyBind-Manager-API
A Python-based keybinding manager designed for Windows systems. This tool allows you to register, unregister, and manage hotkeys to trigger custom actions, supporting complex combinations and cooldowns. It uses ctypes and threading for efficient input monitoring, and provides a simple public API for integration into your projects.



## Features:

- Register hotkeys with key combinations (e.g., ctrl+alt+s)
- Action cooldowns to prevent repeated triggers
- Threaded background listener for non-blocking operation
- Supports keyboard keys, mouse buttons, and multimedia controls

## Usage:

- register_hotkey(combination, action, **kwargs): Register a hotkey.
- unregister_hotkey(combination): Unregister a hotkey.
- start_listening(): Begin listening for hotkeys.
- stop_listening(): Stop listening for hotkeys.
