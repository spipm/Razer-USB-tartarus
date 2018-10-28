# -*- coding: utf-8 -*-
import collections
import uinput

# press key normally
MEAN_PRESS = "press_normal"
# press unicode key
MEAN_PRESSU = "press_unicode"
# press combination
MEAN_COMBO = "press_combo"
# press combination and then a space
MEAN_COMBOS = "press_combo_space"
# use function
MEAN_FUNC = "press_function"


CharMeaning = collections.namedtuple('CharMeaning', ['kind', 'args'])


# This mapping gives meaning to the keys you decribed in the remapping
mapping_meaning = {

  # examples of normal key presses
  "a": CharMeaning(MEAN_PRESS, uinput.KEY_A),
  "b": CharMeaning(MEAN_PRESS, uinput.KEY_B),
  "c": CharMeaning(MEAN_PRESS, uinput.KEY_C),
  "d": CharMeaning(MEAN_PRESS, uinput.KEY_D),
  "e": CharMeaning(MEAN_PRESS, uinput.KEY_E),
  "f": CharMeaning(MEAN_PRESS, uinput.KEY_F),
  "g": CharMeaning(MEAN_PRESS, uinput.KEY_G),
  "h": CharMeaning(MEAN_PRESS, uinput.KEY_H),
  "i": CharMeaning(MEAN_PRESS, uinput.KEY_I),
  "j": CharMeaning(MEAN_PRESS, uinput.KEY_J),
  "k": CharMeaning(MEAN_PRESS, uinput.KEY_K),
  "l": CharMeaning(MEAN_PRESS, uinput.KEY_L),
  "m": CharMeaning(MEAN_PRESS, uinput.KEY_M),
  "n": CharMeaning(MEAN_PRESS, uinput.KEY_N),
  "o": CharMeaning(MEAN_PRESS, uinput.KEY_O),
  "p": CharMeaning(MEAN_PRESS, uinput.KEY_P),
  "q": CharMeaning(MEAN_PRESS, uinput.KEY_Q),
  "r": CharMeaning(MEAN_PRESS, uinput.KEY_R),
  "s": CharMeaning(MEAN_PRESS, uinput.KEY_S),
  "t": CharMeaning(MEAN_PRESS, uinput.KEY_T),
  "u": CharMeaning(MEAN_PRESS, uinput.KEY_U),
  "v": CharMeaning(MEAN_PRESS, uinput.KEY_V),
  "w": CharMeaning(MEAN_PRESS, uinput.KEY_W),
  "x": CharMeaning(MEAN_PRESS, uinput.KEY_X),
  "y": CharMeaning(MEAN_PRESS, uinput.KEY_Y),
  "z": CharMeaning(MEAN_PRESS, uinput.KEY_Z),

  "0": CharMeaning(MEAN_PRESS, uinput.KEY_0),
  "1": CharMeaning(MEAN_PRESS, uinput.KEY_1),
  "2": CharMeaning(MEAN_PRESS, uinput.KEY_2),
  "3": CharMeaning(MEAN_PRESS, uinput.KEY_3),
  "4": CharMeaning(MEAN_PRESS, uinput.KEY_4),
  "5": CharMeaning(MEAN_PRESS, uinput.KEY_5),
  "6": CharMeaning(MEAN_PRESS, uinput.KEY_6),
  "7": CharMeaning(MEAN_PRESS, uinput.KEY_7),
  "8": CharMeaning(MEAN_PRESS, uinput.KEY_8),
  "9": CharMeaning(MEAN_PRESS, uinput.KEY_9),

  "=": CharMeaning(MEAN_PRESS, uinput.KEY_EQUAL),

  "right":  CharMeaning(MEAN_PRESS, uinput.KEY_RIGHT),
  "left":   CharMeaning(MEAN_PRESS, uinput.KEY_LEFT),
  "up":     CharMeaning(MEAN_PRESS, uinput.KEY_UP),
  "down":   CharMeaning(MEAN_PRESS, uinput.KEY_DOWN),

  "pageup": CharMeaning(MEAN_PRESS, uinput.KEY_PAGEUP),
  "pagedown": CharMeaning(MEAN_PRESS, uinput.KEY_PAGEDOWN),

  # example of function key presses
  "kick_ass_macro":  CharMeaning(MEAN_FUNC, "do cool stuff"),

  # example of unicode character
  "french e":  CharMeaning(MEAN_PRESSU, u"é"),
  "strange c": CharMeaning(MEAN_PRESSU, u"ç"),

  # example of combo presses
  "&":  CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTSHIFT, uinput.KEY_7]),
  ":":  CharMeaning(MEAN_COMBO ,[uinput.KEY_LEFTSHIFT, uinput.KEY_SEMICOLON]),
  "(":  CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTSHIFT, uinput.KEY_9]),
  ")":  CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTSHIFT, uinput.KEY_0]),

  "copy":  CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTCTRL, uinput.KEY_C]),
  "paste":  CharMeaning(MEAN_COMBO, [uinput.KEY_LEFTCTRL, uinput.KEY_V]),

  # example of combo that requires additional key (like space)
  "\"": CharMeaning(MEAN_COMBOS, [uinput.KEY_LEFTSHIFT, uinput.KEY_APOSTROPHE]),
  "'":  CharMeaning(MEAN_COMBOS, [uinput.KEY_APOSTROPHE])
}



