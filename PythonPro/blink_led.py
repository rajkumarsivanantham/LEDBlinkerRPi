#!/usr/bin/env python3
"""
Simple LED blinker for Raspberry Pi GPIO.

Connect an LED to the chosen GPIO pin with a current-limiting resistor.
"""

import argparse
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None


def blink_led(pin: int, interval1: float, interval2: float, cycles: int) -> None:
    if GPIO is None:
        raise RuntimeError("RPi.GPIO module is required. Run this on a Raspberry Pi with gpio support.")

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    try:
        for i in range(cycles):
            print(f"Cycle {i + 1}/{cycles}: ON for {interval1}s")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(interval1)

            print(f"Cycle {i + 1}/{cycles}: OFF for {interval2}s")
            GPIO.output(pin, GPIO.LOW)
            time.sleep(interval2)

        print("Blinking complete. Turning LED off.")
    finally:
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Blink an LED on a Raspberry Pi GPIO pin.")
    parser.add_argument("--pin", type=int, default=17, help="BCM GPIO pin number (default: 17)")
    parser.add_argument("--on", type=float, default=0.5, help="LED on interval in seconds (default: 0.5)")
    parser.add_argument("--off", type=float, default=0.5, help="LED off interval in seconds (default: 0.5)")
    parser.add_argument("--cycles", type=int, default=10, help="Number of blink cycles (default: 10)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Starting LED blink on GPIO {args.pin} with on={args.on}s, off={args.off}s, cycles={args.cycles}")
    blink_led(args.pin, args.on, args.off, args.cycles)


if __name__ == "__main__":
    main()
