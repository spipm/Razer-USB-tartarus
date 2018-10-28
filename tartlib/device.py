import uinput

from tartlib.debug import *

from tartlib.mapping.simulate import *
from tartlib.mapping.remap import *
from tartlib.mapping.output import *


class DeviceSimulator():
  """ Human Interface Simulator class """

  def __init__(self):

    self.device = uinput.Device(SIMULATE_KEYS)


  def simulate(self, pressed_keys):
    if pressed_keys in remap_config:

      debugMessage( "Found keys in remap config" )
      mapped_to = remap_config[pressed_keys]

      if mapped_to in mapping_meaning:
        meaning = mapping_meaning[mapped_to]
        
        if meaning.kind == MEAN_PRESS:
          self.device.emit_click(meaning.args)

        elif meaning.kind == MEAN_PRESSU:
          self.press_unicode(meaning.args)

        elif meaning.kind == MEAN_COMBO:
          self.press_combo(meaning.args)

        elif meaning.kind == MEAN_COMBOS:
          self.press_combo(meaning.args, press_space = True)

        elif meaning.kind == MEAN_FUNC:
          # custom stuff
          if meaning.args == "do cool stuff":
            debugMessage("Triggered custom function")

        else:
         debugMessage( "Could not interpret meaning" )

      else:
        debugMessage( "Key mapped but is not assigned meaning :(" )

    else:
      debugMessage( "Could not find key combination in mapping" )


  def press_unicode(self, uni_character):
    # ctrl, shift, u
    self.press_combo(KEY_COMBO_UNICODE)

    # hex characters
    uni_codes_hex = [i for i in hex(ord(uni_character))[2:]]
    for norm_char in uni_codes_hex:
      self.device.emit_click(mapping_meaning[norm_char].args)

    # enter
    self.device.emit_click(uinput.KEY_ENTER)
    

  def press_combo(self, combo, press_space = False):

    self.device.emit_combo(combo)

    if press_space:
      self.device.emit_click(uinput.KEY_SPACE)
