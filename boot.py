import board
import digitalio
import usb_hid
import storage
import usb_midi

enter_pin = board.GP19

# Initializing Button
enter = digitalio.DigitalInOut(enter_pin)
enter.direction = digitalio.Direction.INPUT
enter.pull = digitalio.Pull.DOWN

# Disable devices only if enter button is not pressed.
# Without this logic, the computer will see multiple USB devices
# and the keyboard will not work in the BIOS or boot loader.
if not enter.value:
    storage.disable_usb_drive()
    usb_midi.disable()
    usb_hid.enable((usb_hid.Device.KEYBOARD), boot_device=1)
