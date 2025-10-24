# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\MarioKart8DX_RANDOMIZER_UI_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\MarioKart8DX_RANDOMIZER_UI_autogen.dir\\ParseCache.txt"
  "MarioKart8DX_RANDOMIZER_UI_autogen"
  )
endif()
