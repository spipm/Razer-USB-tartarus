# -*- coding: utf-8 -*-
from tartlib.simulate import *


remapConfig = {

	# remap to letter
	"1":	[combo_norm, mapping_keys["&"]],	
	"2":	[press_unicode, u"é"],
	"3":	[combo_space, mapping_keys["\""]],	
	"4":	[combo_space, mapping_keys["'"]],
	"5":	",",
	"6":	[combo_norm, mapping_keys["("]],
	"7":	"-",
	"8":	[press_unicode, u"è"],
	"9":	[combo_norm, mapping_keys["_"]],
	"10":	";",
	"11":	[press_unicode, u"ç"],
	"12":	[press_unicode, u"à"],
	"13":	[combo_norm, mapping_keys[")"]],
	"14":	"=",
	"15":	[combo_norm, mapping_keys[":"]],

	"ttop":		[doPressPageUp], 	# remap to function for pressing multiple keys
	"tbottom":	[doPressPageDown],

	"up":		"a",
	"right":	"up",
	"down":		"e",
	"left":		"down",

	"1-2-3":	"d" 		# boss mode: map multiple keys
							# don't use this yet: implementation is harder
}
