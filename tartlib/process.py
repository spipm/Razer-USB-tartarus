import uinput

from tartlib.mapping import *
from tartlib.debug import *
from tartlib.simulate import *

RELEASE_COMBO = [0, 0, 0, 0, 0, 0, 0, 0]
EXIT_COMMAND = ["12","13","14","15","TTOP"]



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

  debugMessage( "User is pressing keys: %s" % ','.join(pressed_keys) )

  # exit command
  if pressed_keys == EXIT_COMMAND:
    debugMessage( "Exit command.." )
    return -1

  if pressed_keys == ["3"]:
    debugMessage( "Performing cut.." )
    doCutzxcv()

  if pressed_keys == ["4"]:
    debugMessage( "Performing copy.." )
    doCopy()

  if pressed_keys == ["5"]:
    debugMessage( "Performing paste.." )
    doPaste()

  if pressed_keys == ["TTOP"]:
    debugMessage( "Creating new tab.." )
    doNewTab()

  if pressed_keys == ["TBOTTOM"]:
    debugMessage( "Closing tab.." )
    doCloseTab()

  if pressed_keys == ["10"]:
    debugMessage( "Changing tab.." )
    doChangeTab()

  if pressed_keys == ["9"]:
    debugMessage( "Changing window.." )
    doChangeWindow()

  if pressed_keys == ["UP"]:
    debugMessage( "Scrolling to top.." )
    doPressHome()

  if pressed_keys == ["DOWN"]:
    debugMessage( "Scrolling to bottom.." )
    doPressEnd()

  if pressed_keys == ["LEFT"]:
    debugMessage( "Page down.." )
    doPressPageDown()

  if pressed_keys == ["RIGHT"]:
    debugMessage( "Page up.." )
    doPressPageUp()

  old_presses = pressed_keys
