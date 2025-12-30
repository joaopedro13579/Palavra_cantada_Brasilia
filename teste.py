import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_LIST = [
    4, 5, 6, 12, 13,
    16, 17, 18, 19,
    20, 21, 22, 23,
    24, 25, 26, 27
]

results = {
    "outputs": {},
    "inputs": {}
}

# -------------------------
# PHASE 1: LED TEST (MANUAL CONFIRM)
# -------------------------
print("\n🔧 LED OUTPUT TEST")
print("Answer y/n for each GPIO\n")

for pin in GPIO_LIST:
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

        answer = input(f"GPIO {pin}: Did the LED turn ON? (y/n): ").strip().lower()

        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup(pin)

        if answer == "y":
            results["outputs"][pin] = "ok"
        else:
            results["outputs"][pin] = "failed"

    except Exception as e:
        results["outputs"][pin] = f"error: {e}"

print("\n✅ LED test finished\n")
time.sleep(1)

# -------------------------
# PHASE 2: BUTTON TEST
# -------------------------
print("🔘 BUTTON INPUT TEST")
print("Press each button once (you have 15 seconds)\n")

def button_callback(channel):
    results["inputs"][channel] = "pressed"
    print(f"Button detected on GPIO {channel}")

for pin in GPIO_LIST:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    results["inputs"][pin] = "not_pressed"
    GPIO.add_event_detect(pin, GPIO.FALLING,
                          callback=button_callback,
                          bouncetime=200)

time.sleep(15)

GPIO.cleanup()

# -------------------------
# SAVE RESULTS
# -------------------------
with open("gpio_test_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\n📄 Results saved to gpio_test_results.json")
print("🟢 Test complete")
