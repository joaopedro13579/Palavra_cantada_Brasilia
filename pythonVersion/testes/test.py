import RPi.GPIO as GPIO
import time

# =======================
# BASIC SETUP
# =======================
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ALL_GPIO = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26
]

# =======================
# UTILITIES
# =======================
def wait(msg="Press ENTER to continue"):
    input(msg)

def yes_no(msg):
    return input(msg + " (y/n): ").strip().lower() == "y"

# =======================
# BUTTON TEST
# =======================
def test_buttons():
    print("\n=== BUTTON CATALOG TEST ===")
    print("Apply 3.3V to ONE button at a time")

    button_map = {}

    for pin in ALL_GPIO:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Waiting for button presses...")
    print("Press CTRL+C to stop\n")

    try:
        while True:
            for pin in ALL_GPIO:
                if GPIO.input(pin):
                    print(f"\nDetected HIGH on GPIO {pin}")
                    name = input("Enter button name/ID: ")
                    button_map[name] = pin
                    time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    print("\nBUTTON MAP:")
    for k, v in button_map.items():
        print(f"{k} → GPIO {v}")

    return button_map

# =======================
# LED TEST
# =======================
def test_leds():
    print("\n=== LED CATALOG TEST ===")
    led_map = {}

    for pin in ALL_GPIO:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    for pin in ALL_GPIO:
        print(f"\nTesting GPIO {pin}")
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)

        if yes_no("Is any LED ON?"):
            name = input("Enter LED name/ID: ")
            led_map[name] = pin

        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.3)

    print("\nLED MAP:")
    for k, v in led_map.items():
        print(f"{k} → GPIO {v}")

    return led_map

# =======================
# POTENTIOMETER (ADS1115)
# =======================
def test_ads1115():
    print("\n=== ADS1115 POTENTIOMETER TEST ===")

    import board
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn

    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)

    chan = AnalogIn(ads, ADS.P0)

    print("Rotate the potentiometer (CTRL+C to stop)")
    try:
        while True:
            print(f"Voltage: {chan.voltage:.3f} V")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

# =======================
# MAIN MENU
# =======================
def main():
    print("""
==============================
GPIO COMMISSIONING TEST
==============================
1 - Potentiometer (ADS1115)
2 - LED / Button Map
3 - Button / Video Machine
""")

    choice = input("Select machine type: ").strip()

    if choice == "1":
        test_ads1115()

    elif choice == "2":
        buttons = test_buttons()
        wait()
        leds = test_leds()

    elif choice == "3":
        print("\nButton → Video mapping test")
        test_buttons()

    else:
        print("Invalid selection")

    GPIO.cleanup()
    print("\nTest complete. GPIO cleaned up.")

if __name__ == "__main__":
    main()
