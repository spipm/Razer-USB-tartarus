#!/usr/bin/python
import usb.core
import usb.util

import uinput

# Example that allows copy-pasting using the tartarus buttons 4 and 5

# http://tjjr.fi/sw/python-uinput/
# https://www.orangecoat.com/how-to/read-and-decode-data-from-your-mouse-using-this-pyusb-hack


# how to we call the thumb buttons?
THUMB_TOP_BUTTON_NAME = "TTOP"
THUMB_BOTTOM_BUTTON_NAME = "TBOTTOM"

# Mapping for the Razer Tartarus Chroma

mapping_normal = {
# Normal number keys
0x2b:"1",
0x14:"2",
0x1a:"3",
0x08:"4",
0x15:"5",
0x39:"6",
0x04:"7",
0x16:"8",
0x07:"9",
0x09:"10",
0x1d:"12",
0x1b:"13",
0x06:"14",
0x19:"15",
# thumb keys
0x2c:THUMB_BOTTOM_BUTTON_NAME,
0x50:"UP",
0x52:"RIGHT",
0x4f:"DOWN",
0x51:"LEFT"
}

mapping_special = {
# Special keys (first byte)
0x02:"11",
0x04:THUMB_TOP_BUTTON_NAME,
0x06:"11+%s" % THUMB_TOP_BUTTON_NAME
}

device = uinput.Device([
  uinput.KEY_LEFTCTRL,
  uinput.KEY_C,
  uinput.KEY_V
  ])

def doCopy():
  device.emit_combo([uinput.KEY_LEFTCTRL,uinput.KEY_C])

def doPaste():
  device.emit_combo([uinput.KEY_LEFTCTRL,uinput.KEY_V])


def processPresses(data):
  if data == [0, 0, 0, 0, 0, 0, 0, 0]:
    print "User released all buttons"
    return

  pressed_keys = [mapping_normal[i] for i in data[2:] if i != 0]
  print "User is pressing keys: %s" % ','.join(pressed_keys) 

  if data[0] != 0:
    pressed_special_keys = mapping_special[data[0]]
    print "User is pressing special keys: %s" % pressed_special_keys

  if "4" in pressed_keys:
    print "Performing copy.."
    doCopy()
  if "5" in pressed_keys:
    print "Performing paste.."
    doPaste()



dev = usb.core.find(idVendor=0x1532, idProduct=0x0208)
interface = 0
endpoint = dev[0][(0,0)][0]
if dev.is_kernel_driver_active(interface) is True:
  dev.detach_kernel_driver(interface)
  usb.util.claim_interface(dev, interface)


for i in range(32):
    try:
        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        print "%i = %s" % (i, data)
        
        pressedData = data.tolist()
        processPresses(pressedData)

    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue


usb.util.release_interface(dev, interface)
dev.attach_kernel_driver(interface)