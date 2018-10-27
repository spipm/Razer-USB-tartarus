import uinput

from tartlib.debug import *
from tartlib.simulate import *

from remapconf import *


RELEASE_COMBO = [0, 0, 0, 0, 0, 0, 0, 0]
EXIT_COMMAND = "12-13-14-15-ttop"



old_presses = None


def processData(data):
  global old_presses

  data = data.tolist()
  
  if data == RELEASE_COMBO:
    debugMessage( "User released all buttons" )
    return

  pressed_keys = [mapping_normal[i] for i in data[2:] if i != 0]

  if data[0] != 0:
    pressed_special_keys = mapping_special[data[0]]
    pressed_keys.append(pressed_special_keys)

  pressed_keys = '-'.join(pressed_keys)

  debugMessage( "User is pressing keys: %s" %  pressed_keys)

  # exit command
  if pressed_keys == EXIT_COMMAND:
    debugMessage( "Exit command.." )
    return -1

  if pressed_keys in remapConfig:
    debugMessage( "Found key" )
    mapTo = remapConfig[pressed_keys]

    if isinstance(mapTo, basestring):
      debugMessage( "Pressing %s" % mapTo )
      doClickKey(mapping_keys[mapTo])

    else:
      debugMessage( "Executing %s" % mapTo.__name__ )
      mapTo()

  else:
    debugMessage( "Could not find key combination in mapping" )
    debugMessage( "Combination was:" )
    debugMessage( pressed_keys )

  old_presses = pressed_keys
