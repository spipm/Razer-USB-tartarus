
from tartlib.mapping.hardware import *
from tartlib.mapping.state import *

from tartlib.debug import *
from tartlib.device import DeviceSimulator



class TartDataProcessor():
  """ Processor for data from Razer Tartarus """

  def __init__(self):

    self.old_presses = ""

    self.RELEASE_COMBO = HARDWARE_MAPPING_RELEASE_COMBO
    self.EXIT_COMMAND = HARDWARE_MAPPING_EXIT_COMMAND

    self.simulator = DeviceSimulator()


  def processData(self, data):
    ''' Process raw data from Tartarus '''

    data = data.tolist()
    
    if data == self.RELEASE_COMBO:
      debugMessage( "User released all buttons" )
      return 0

    pressed_keys = [hardware_mapping_normal[i] for i in data[2:] if i != 0]

    if data[0] != 0:
      pressed_special_keys = hardware_mapping_special[data[0]]
      pressed_keys.append(pressed_special_keys)

    pressed_keys = '-'.join(pressed_keys)
    debugMessage( "User is pressing keys: %s" %  pressed_keys)

    # check for exit command
    if pressed_keys == self.EXIT_COMMAND:
      debugMessage( "Exit command.." )
      return -1

    # handle state change here?
    state = "%s=>%s" % (self.old_presses, pressed_keys)
    if state in state_mapping:
      debugMessage("Found state in mapping :) state:")
      debugMessage( state )

    # handle key presses
    self.simulator.simulate(pressed_keys)

    # save old key presses
    self.old_presses = pressed_keys

    return 0
