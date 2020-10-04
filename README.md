# qtpy-keys
Tiny USB keyboard using QTPy and CircuitPython

- Three touch sensors, each send a different key (LEFT_ARROW, UP_ARROW, DOWN_ARROW by default)
- R,G,B LEDs light up when a key is pressed

The QT Py has minimal flash space so copying full `adafruit_hid` library
may not work. So the included pre-built `lib` directory zipfile
contains everything needed.

Also on a Mac, copying files generates 4kB "._" meta files that fill up the
QT Py's disk space quickly.  To prevent this, you need to set this preference and
restart the finder:
```
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
killall Finder
```
Then you can unzip this lib.zip.

To install:

```
cd ~/Downloads
git clone https://github.com/todbot/qtpy-keys
cd /Volumes/CIRCUITPY
cp ~/Downloads/qtpy-keys/code.py .
rm -rf lib
unzip ~/Downloads/qtpy-keys/qtpy-keys-lib.zip 
```
<img src="qtpy-keys-demo.gif"/>


