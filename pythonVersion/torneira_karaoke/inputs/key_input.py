# input/key_input.py

import keyboard

class KeyInput:
    def __init__(self, callback):
        self.callback = callback

    def start(self):
        for key in ["1", "2", "3"]:
            keyboard.on_press_key(key, self._handle)

        keyboard.wait()

    def _handle(self, event):
        self.callback(event.name)
