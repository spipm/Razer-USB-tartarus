#!/usr/bin/python
from tartlib.usbkernel import *
from tartlib.process import *


# Get the device and claim it from the 
try:
  dev = getDevice(0x1532, 0x0208) # 0x1532 = razer, 0x0208 = tartarus
  claimInterface(dev)
  endpoint = dev[0][(0,0)][0]

except Exception as e:
  raise

try:

  while True:

    try:

      data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
      ret = processData(data)

      if ret == -1:
        break

    except usb.core.USBError as e:
      if e.args == ('Operation timed out',):
        continue

except:
  raise

finally:
  if dev is not None:
    releaseDevice(dev)
