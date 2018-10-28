# Razer-USB-tartarus
Using the Razer Tartarus Chroma on Linux

OpenRazer tools didn't work like I wanted to so I made my own script to interact with the Razer Tartarus Chroma.

## Usage
* This should about fix deps:
`pip install python-uinput pyusb`
* Change configuration, see below
* Plug in Tartarus, run script:
`sudo python run.py`
* If you're done, press 12-13-14-15-[top thumb button] at the same time to quit

Run the usbreset.c program if your device starts acting weird.

## Configuration

#### 1. Map values in `remap.py`. 

The dictionary remap_config allows you to bind values from the Tartarus input to psuedo values. Only change the values on the right. You can choose random mapping names.

Example:

`"1":	"strange c",`

This maps the 1 on the Tartarus to the psuedo value "strange c"

Example:

`"14-11":	"copy",`

This maps pressing 11 and 14 at the same time to the psuedo value "copy"

#### 2. Change mapping meaning in `output.py`

Use the dictionary `mapping_meaning` to assign meaning to the psuedo values you described in step 1. The following functionality is available:

* MEAN_PRESS - Enter normal character:
  * Example: `"a": CharMeaning(MEAN_PRESS, uinput.KEY_A),`
  * This simulates pressing the a-key

* MEAN_PRESSU - Enter unicode character:
  * Example: `"strange c": CharMeaning(MEAN_PRESSU, u"ç"),`
  * This simulates pressing the unicode character ç. It does so by pressing ctrl+shift+u, then the unicode value in hex, then the enter key. Not that some programs will hijack key combination which could breaks this.

* MEAN_COMBO - Press combination
  * Example: `"&": CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTSHIFT, uinput.KEY_7]),`
  * This simulates pressing shift+7

* MEAN_COMBOS - Press combination and then a space
  * Example: `"\"": CharMeaning(MEAN_COMBOS, [uinput.KEY_LEFTSHIFT, uinput.KEY_APOSTROPHE]),`
  * This simulates pressing shift+7 and then a space
  
* MEAN_FUNC - Trigger custom functionality
  * Example: `"kick_ass_macro":  CharMeaning(MEAN_FUNC, "do cool stuff"),`
  * This just defined custom functionality you can use in `device.py` to create custom macro's
  
A full list of input keys can be found here:
https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h
If you need additional keys make sure they are included in `SIMULATE_KEYS` in `simulate.py`, or the device simulator won't be able to simulate them.

## Stuff
You can actually to more than with the original Razer software! The original software only allows you to configure one key at a time. But the device supports pressing up to 8 keys at once.

* We get 8 bytes of data
* Starting from byte 3, we get the buttons a user is pressing
* If all bytes are zero, user has released all buttons

You can even program this script to trigger commands when keys are pressed (simoultaniously) in a certain order.
