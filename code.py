# qtpy-keys -- tiny keyboard using QTPy
# 1 Oct 2020 - @todbot
import time
import board 
import neopixel
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

touchA= touchio.TouchIn(board.A0)
touchB= touchio.TouchIn(board.A1)
touchC= touchio.TouchIn(board.A2)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2, auto_write=False)
pixel[0] = (0,0,0)

print("qtpy-keys!")
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
kbd = Keyboard(usb_hid.devices)

while True:
    if touchA.value:
        print("A press")
        pixel[0] = (255,0,0)
        kbd.send(Keycode.RIGHT_ARROW)
    if touchB.value:
        print("B press")
        pixel[0] = (0,255,0)
        kbd.send(Keycode.UP_ARROW)
    if touchC.value:
        print("C press")
        pixel[0] = (0,0,255)
        kbd.send(Keycode.LEFT_ARROW)
    pixel.show()
    pixel[0] = (0,0,0)
    time.sleep(0.2)

    
