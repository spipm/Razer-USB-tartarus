# how to we call the thumb buttons?
THUMB_TOP_BUTTON_NAME = "ttop"
THUMB_BOTTOM_BUTTON_NAME = "tbottom"

# Mapping for the Razer Tartarus Chroma hardware input

hardware_mapping_normal = {
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

hardware_mapping_special = {
  # Special keys (first byte)
  0x02:"11",
  0x04:THUMB_TOP_BUTTON_NAME,
  0x06:"11+%s" % THUMB_TOP_BUTTON_NAME
}

HARDWARE_MAPPING_RELEASE_COMBO = [0, 0, 0, 0, 0, 0, 0, 0]
HARDWARE_MAPPING_EXIT_COMMAND = "12-13-14-15-ttop"