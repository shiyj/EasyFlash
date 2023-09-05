cmake_minimum_required(VERSION 3.1)

include(mc_arm_gcc)

mc_set_arm_gcc()

project(EasyFlash C ASM)

mc_set_include_list(
   ./easyflash/inc
)

mc_set_source_list(
   ./easyflash/src/*.c
)

mc_export_library()

