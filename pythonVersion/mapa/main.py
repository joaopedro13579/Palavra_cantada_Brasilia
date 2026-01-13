import json
import subprocess
import time

# ========================
# GPIO SETUP (commented)
# ========================
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# LED_PINS = {
#     1: 17,
#     2: 27,
#     3: 22,
#     4: 23,
#     5: 24
# }
# for pin in LED_PINS.values():
#     GPIO.setup(pin, GPIO.OUT)

# ========================
# LOAD CONFIG
# ========================
with open("config.json") as f:
    CONFIG = json.load(f)["buttons"]

# ========================
# LED CONTROL (mock)
# ========================
def led_on(led_id):
    print(f"[LED {led_id}] ON")
    # GPIO.output(LED_PINS[led_id], GPIO.HIGH)

def led_off(led_id):
    print(f"[LED {led_id}] OFF")
    # GPIO.output(LED_PINS[led_id], GPIO.LOW)

# ========================
# AUDIO PLAYER
# ========================
def play_audio(file):
    print(f"[AUDIO] Playing {file}")
    subprocess.run(["mpv", "--no-video", file])

# ========================
# MAIN LOOP (keyboard = buttons)
# ========================
print("Press keys 1–9 or 0 (ESC to quit)")

try:
    while True:
        key = input("Button: ").strip()

        if key.lower() == "esc":
            break

        if key not in CONFIG:
            print("Invalid button")
            continue

        led_id = CONFIG[key]["led"]
        audio = CONFIG[key]["audio"]

        led_on(led_id)
        play_audio(audio)
        led_off(led_id)

        time.sleep(0.2)

finally:
    print("Exiting...")
    # GPIO.cleanup()
