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
 
  "up":     CharMeaning(MEAN_PRESS, uinput.KEY_UP),
  "down":   CharMeaning(MEAN_PRESS, uinput.KEY_DOWN),

  # example of unicode character

  "esperluette": CharMeaning(MEAN_PRESSU, u"&"),
  "e aigu": CharMeaning(MEAN_PRESSU, u"é"),
  "petit deux": CharMeaning(MEAN_PRESSU, u"²"),
  "apostrophe": CharMeaning(MEAN_PRESSU, u"'"),
  "virgule": CharMeaning(MEAN_PRESSU, u","),
  "parent gauche": CharMeaning(MEAN_PRESSU, u"("),
  "moins": CharMeaning(MEAN_PRESSU, u"-"),
  "e grave": CharMeaning(MEAN_PRESSU, u"è"),
  "souligne": CharMeaning(MEAN_PRESSU, u"_"),
  "point virgule": CharMeaning(MEAN_PRESSU, u";"),
  "cedille": CharMeaning(MEAN_PRESSU, u"ç"),
  "a accent": CharMeaning(MEAN_PRESSU, u"à"),
  "parent droite": CharMeaning(MEAN_PRESSU, u")"),
  "egal": CharMeaning(MEAN_PRESSU, u"="),
  "deux points": CharMeaning(MEAN_PRESSU, u":"),
  "exclamation": CharMeaning(MEAN_PRESSU, u"!"),
  "u accent": CharMeaning(MEAN_PRESSU, u"ù"),
  "a": CharMeaning(MEAN_PRESSU, u"a"),
  "e": CharMeaning(MEAN_PRESSU, u"e")

}


