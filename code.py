import board
import digitalio
import time
import usb_hid
import storage
import usb_midi
from usb_hid import Device
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print('booting up')

# Set pins for buttons
up_pin = board.GP7
enter_pin = board.GP19
down_pin = board.GP10

# Initializing Button
up = digitalio.DigitalInOut(up_pin)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.DOWN

enter = digitalio.DigitalInOut(enter_pin)
enter.direction = digitalio.Direction.INPUT
enter.pull = digitalio.Pull.DOWN

down = digitalio.DigitalInOut(down_pin)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

print('starting main loop')
while True:
    if up.value:
        print(" up button Pressed")
        keyboard.press(Keycode.UP_ARROW)
        time.sleep(0.15)
        keyboard.release(Keycode.UP_ARROW)
    if enter.value:
        print(" enter button Pressed")
        keyboard.press(Keycode.ENTER)
        time.sleep(0.15)
        keyboard.release(Keycode.ENTER)
    if down.value:
        print(" down button Pressed")
        keyboard.press(Keycode.DOWN_ARROW)
        time.sleep(0.15)
        keyboard.release(Keycode.DOWN_ARROW)
    time.sleep(0.1)
