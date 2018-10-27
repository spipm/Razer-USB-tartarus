import usb.core
import usb.util


def getDevice(vendorID, productID):
  ''' Return the device object '''

  dev = usb.core.find(idVendor=vendorID, idProduct=productID)

  if dev is None:
    raise ValueError('Device not found')

  return dev


def claimInterface(dev, interface=0):

  if dev.is_kernel_driver_active(interface) is True:
    dev.detach_kernel_driver(interface)
    usb.util.claim_interface(dev, interface)


def releaseDevice(dev, interface=0):
  ''' Release device and attach kernel back '''

  usb.util.release_interface(dev, interface)
  dev.attach_kernel_driver(interface)

