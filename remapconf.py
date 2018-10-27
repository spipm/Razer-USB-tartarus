from tartlib.simulate import *

remapConfig = {
	"1":	"a",	# remap to letter
	"2":	"a",
	"3":	"a",	
	"4":	"a",
	"5":	"a",
	"6":	"b",
	"7":	"b",
	"8":	"b",
	"9":	"b",
	"10":	"b",
	"11":	"c",
	"12":	"c",
	"13":	"c",
	"14":	"c",
	"15":	"c",
	
	"1-2-3":	"d", 		# boss mode: map multiple keys
							# don't use this yet: implementation is harder

	"ttop":		doNewTab, 	# remap to function for pressing multiple keys
	"tbottom":	doCloseTab,

	"up":		"up",
	"right":	"right",
	"down":		"down",
	"left":		"left",
}

