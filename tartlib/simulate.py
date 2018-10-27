import uinput


# init device
device = uinput.Device([
  uinput.KEY_ENTER,
  uinput.KEY_SPACE,

  uinput.KEY_LEFTCTRL,
  uinput.KEY_LEFTSHIFT,
  uinput.KEY_LEFTALT,
  uinput.KEY_TAB,

  uinput.KEY_HOME,
  uinput.KEY_END,
  uinput.KEY_PAGEDOWN,
  uinput.KEY_PAGEUP,

  uinput.KEY_A,
  uinput.KEY_B,
  uinput.KEY_C,
  uinput.KEY_D,
  uinput.KEY_E,
  uinput.KEY_F,
  uinput.KEY_G,
  uinput.KEY_H,
  uinput.KEY_I,
  uinput.KEY_J,
  uinput.KEY_K,
  uinput.KEY_L,
  uinput.KEY_M,
  uinput.KEY_N,
  uinput.KEY_O,
  uinput.KEY_P,
  uinput.KEY_Q,
  uinput.KEY_R,
  uinput.KEY_S,
  uinput.KEY_T,
  uinput.KEY_U,
  uinput.KEY_V,
  uinput.KEY_W,
  uinput.KEY_X,
  uinput.KEY_Y,
  uinput.KEY_Z,

  uinput.KEY_0,
  uinput.KEY_1,
  uinput.KEY_2,
  uinput.KEY_3,
  uinput.KEY_4,
  uinput.KEY_5,
  uinput.KEY_6,
  uinput.KEY_7,
  uinput.KEY_8,
  uinput.KEY_9,

  uinput.KEY_RIGHT,
  uinput.KEY_LEFT,
  uinput.KEY_UP,
  uinput.KEY_DOWN,

  uinput.KEY_APOSTROPHE,
  uinput.KEY_COMMA,
  uinput.KEY_MINUS,
  uinput.KEY_EQUAL,
  uinput.KEY_SEMICOLON

  ])


# create key combinations
KEY_COMBO_CUT = [uinput.KEY_LEFTCTRL,uinput.KEY_X]
KEY_COMBO_COPY = [uinput.KEY_LEFTCTRL,uinput.KEY_C]
KEY_COMBO_PASTE = [uinput.KEY_LEFTCTRL,uinput.KEY_V]

KEY_COMBO_TAB_CHANGE = [uinput.KEY_LEFTCTRL,uinput.KEY_TAB]
KEY_COMBO_TAB_NEW = [uinput.KEY_LEFTCTRL,uinput.KEY_T]
KEY_COMBO_TAB_CLOSE = [uinput.KEY_LEFTCTRL,uinput.KEY_W]

KEY_COMBO_WINDOW_CLOSE = [uinput.KEY_LEFTALT,uinput.KEY_TAB]

KEY_COMBO_UNICODE = [uinput.KEY_LEFTCTRL, uinput.KEY_LEFTSHIFT, uinput.KEY_U]

# how to we call the thumb buttons?
THUMB_TOP_BUTTON_NAME = "ttop"
THUMB_BOTTOM_BUTTON_NAME = "tbottom"

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
  0x50:"up",
  0x52:"right",
  0x4f:"down",
  0x51:"left"
}

mapping_special = {
  # Special keys (first byte)
  0x02:"11",
  0x04:THUMB_TOP_BUTTON_NAME,
  0x06:"11+%s" % THUMB_TOP_BUTTON_NAME
}

# key mapping for easy remapping
mapping_keys = {
  "a": uinput.KEY_A,
  "b": uinput.KEY_B,
  "c": uinput.KEY_C,
  "d": uinput.KEY_D,
  "e": uinput.KEY_E,
  "f": uinput.KEY_F,
  "g": uinput.KEY_G,
  "h": uinput.KEY_H,
  "i": uinput.KEY_I,
  "j": uinput.KEY_J,
  "k": uinput.KEY_K,
  "l": uinput.KEY_L,
  "m": uinput.KEY_M,
  "n": uinput.KEY_N,
  "o": uinput.KEY_O,
  "p": uinput.KEY_P,
  "q": uinput.KEY_Q,
  "r": uinput.KEY_R,
  "s": uinput.KEY_S,
  "t": uinput.KEY_T,
  "u": uinput.KEY_U,
  "v": uinput.KEY_V,
  "w": uinput.KEY_W,
  "x": uinput.KEY_X,
  "y": uinput.KEY_Y,
  "z": uinput.KEY_Z,

  "0": uinput.KEY_0,
  "1": uinput.KEY_1,
  "2": uinput.KEY_2,
  "3": uinput.KEY_3,
  "4": uinput.KEY_4,
  "5": uinput.KEY_5,
  "6": uinput.KEY_6,
  "7": uinput.KEY_7,
  "8": uinput.KEY_8,
  "9": uinput.KEY_9,

  "right": uinput.KEY_RIGHT,
  "left": uinput.KEY_LEFT,
  "up": uinput.KEY_UP,
  "down": uinput.KEY_DOWN,

  "&": [uinput.KEY_LEFTSHIFT, uinput.KEY_7],
  # Enter required depends on keyboard settings
  "\"": [uinput.KEY_LEFTSHIFT, uinput.KEY_APOSTROPHE],
  "'": [uinput.KEY_APOSTROPHE],
  ",": uinput.KEY_COMMA,
  "(": [uinput.KEY_LEFTSHIFT, uinput.KEY_9],
  ")": [uinput.KEY_LEFTSHIFT, uinput.KEY_0],
  "-": uinput.KEY_MINUS,
  "_": [uinput.KEY_LEFTSHIFT, uinput.KEY_MINUS],
  "=": uinput.KEY_EQUAL,
  ";": uinput.KEY_SEMICOLON,
  ":": [uinput.KEY_LEFTSHIFT, uinput.KEY_SEMICOLON],
  "!": [uinput.KEY_LEFTSHIFT, uinput.KEY_1]
}

# remapping functions
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

def doClickKey(key):
  device.emit_click(key)

def press_unicode(uni_character):
  # ctrl, shift, u
  device.emit_combo(KEY_COMBO_UNICODE)
  # hex characters
  uni_codes_hex = [i for i in hex(ord(uni_character))[2:]]
  for norm_char in uni_codes_hex:
    device.emit_click(mapping_keys[norm_char])
  # enter
  device.emit_click(uinput.KEY_ENTER)

def combo_space(combo, press_space = True):
  device.emit_combo(combo)
  if press_space:
    device.emit_click(uinput.KEY_SPACE)

def combo_norm(combo):
  combo_space(combo, press_space = False)