# LED Blinker

A simple Python script to blink an LED connected to a Raspberry Pi GPIO pin.

## Files

- `blink_led.py` - Main script that toggles a GPIO pin on/off at configurable intervals.

## Requirements

- Raspberry Pi with GPIO support
- Python 3
- `RPi.GPIO` library installed

## Hardware Setup

1. Connect the LED's anode (long lead) to a Raspberry Pi GPIO pin, e.g. BCM 17.
2. Connect the LED's cathode (short lead) through a current-limiting resistor (220–330Ω) to a ground pin.
3. Use the BCM pin numbering mode in the script.

## Usage

Run the script from the project folder:

```bash
python blink_led.py --pin 17 --on 0.5 --off 0.5 --cycles 10
```

### Command-line options

- `--pin` — BCM GPIO pin number (default: `17`)
- `--on` — LED ON interval in seconds (default: `0.5`)
- `--off` — LED OFF interval in seconds (default: `0.5`)
- `--cycles` — Number of blink cycles (default: `10`)

## Example

```bash
python blink_led.py --pin 18 --on 0.2 --off 0.8 --cycles 20
```

## Notes

- The script uses `RPi.GPIO` and must be run on a Raspberry Pi or compatible board.
- If the library is not installed, install it with:

```bash
pip install RPi.GPIO
```

- The script cleans up the GPIO state after completion.
