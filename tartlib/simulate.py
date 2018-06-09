import uinput


KEY_COMBO_CUT = [uinput.KEY_LEFTCTRL,uinput.KEY_X]
KEY_COMBO_COPY = [uinput.KEY_LEFTCTRL,uinput.KEY_C]
KEY_COMBO_PASTE = [uinput.KEY_LEFTCTRL,uinput.KEY_V]

KEY_COMBO_TAB_CHANGE = [uinput.KEY_LEFTCTRL,uinput.KEY_TAB]
KEY_COMBO_TAB_NEW = [uinput.KEY_LEFTCTRL,uinput.KEY_T]
KEY_COMBO_TAB_CLOSE = [uinput.KEY_LEFTCTRL,uinput.KEY_W]

KEY_COMBO_WINDOW_CLOSE = [uinput.KEY_LEFTALT,uinput.KEY_TAB]


device = uinput.Device([
  uinput.KEY_LEFTCTRL,
  uinput.KEY_LEFTALT,
  uinput.KEY_TAB,

  uinput.KEY_HOME,
  uinput.KEY_END,
  uinput.KEY_PAGEDOWN,
  uinput.KEY_PAGEUP,

  uinput.KEY_C,
  uinput.KEY_V,
  uinput.KEY_X,
  uinput.KEY_T,
  uinput.KEY_W
  ])


def doCut():
  device.emit_combo(KEY_COMBO_CUT)

def doCopy():
  device.emit_combo(KEY_COMBO_COPY)

def doPaste():
  device.emit_combo(KEY_COMBO_PASTE)

def doChangeTab():
  device.emit_combo(KEY_COMBO_TAB_CHANGE)

def doNewTab():
  device.emit_combo(KEY_COMBO_TAB_NEW)

def doCloseTab():
  device.emit_combo(KEY_COMBO_TAB_CLOSE)

def doChangeWindow():
  device.emit_combo(KEY_COMBO_WINDOW_CLOSE)


def doPressHome():
  device.emit_click(uinput.KEY_HOME)

def doPressEnd():
  device.emit_click(uinput.KEY_END)

def doPressPageDown():
  device.emit_click(uinput.KEY_PAGEDOWN)

def doPressPageUp():
  device.emit_click(uinput.KEY_PAGEUP)





