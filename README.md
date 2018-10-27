# Razer-USB-tartarus
Using the Razer Tartarus Chroma on Linux

OpenRazer tools didn't work like I wanted to so I made my own script to interact with the Razer Tartarus Chroma.

## Usage
* This should about fix deps:
`pip install python-uinput pyusb`
* Change remapconf.py for configuring certain keys
* Plug in Tartarus, run script:
`sudo python run.py`
* If you're done, press 12-13-14-15-[top thumb button] at the same time to quit

Run the usbreset.c program if your device starts acting weird.

## Stuff
You can actually to more than with the original Razer software! The original software only allows you to configure one key at a time. But the device supports pressing up to 8 keys at once.

* We get 8 bytes of data
* Starting from byte 3, we get the buttons a user is pressing
* If all bytes are zero, user has released all buttons

You can even program this script to trigger commands when keys are pressed (simoultaniously) in a certain order.

