# inputs/input_manager.py

# ===== GPIO VERSION (DESATIVADA) =====
# from gpiozero import Button
#
# class GPIOInput:
#     def __init__(self, callback):
#         self.callback = callback
#         self.buttons = {
#             "1": Button(17),
#             "2": Button(27),
#             "3": Button(22),
#         }
#
#     def start(self):
#         for key, button in self.buttons.items():
#             button.when_pressed = lambda k=key: self.callback(k)
#
#         while True:
#             pass


# ===== KEYBOARD VERSION (ATIVA) =====
from inputs.key_input import KeyInput


def get_input_handler(callback):
    return KeyInput(callback)
