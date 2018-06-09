#!/usr/bin/python
import usb.core
import usb.util

#
# This script will read 32 lines of USB data from the tartarus chroma
# Can be used to check how button presses are sent
# 

# https://www.orangecoat.com/how-to/read-and-decode-data-from-your-mouse-using-this-pyusb-hack

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

    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue


usb.util.release_interface(dev, interface)
dev.attach_kernel_driver(interface)