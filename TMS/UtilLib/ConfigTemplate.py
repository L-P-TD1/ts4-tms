"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TwelfthDoctor1's Teleport Memory System

> Config Template

(C) Copyright TD1 & TWoCC 2020 - 2021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Licensed under MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Codes from other parties are not part of the License and Copyright.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# ======================================================================================================================
# DEFAULT CONFIGURATION FILE
# This is the default settings for the config file (in .json)
#
# JSON Methodology make use of Python Dictionaries, thereby simplifying
# addition, deletion, and modification processes.
#
# Ensure that the keys are UNIQUE. Also ensure that the keys in code FULLY MATCH
# those written here, or else an error will occur inferring that the key does not exist.
#
# Default values can either be set from here for in UI via value. However, it is recommended to do it here instead.

CONFIG_NAME = "TD1_TMS_Settings"  # Name of Config File
CONFIG_DEFAULT = {
    'disable_notifs': False,
    'wellness_tms_autoadd': True,
    'vampire_bat_tms_autoadd': True,
    'vampire_mist_tms_autoadd': True,
    'vampire_run_tms_autoadd': True,
    'witch_spell_autoadd': True,
    'witch_broom_tms_autoadd': True,
    'td1_dark_apparate_tms_autoadd': True,
    'td1_mist_spell_tms_autoadd': True,
    'td1_bat_spell_tms_autoadd': True,
    'td1_run_spell_tms_autoadd': True,
    'pet_teleport_tms_autoadd': True,
    'cheat_debug_pie_menu': False,
    'vampire_bat_distance': 1,
    'vampire_mist_distance': 1,
    'witch_spell_distance': 7,
    'witch_broom_distance': 40,
    'werewolf_run_tms_autoadd': True,
    'ghost_teleport_tms_autoadd': True,
    'spacebend_teleport_tms_autoadd': True,
    'ghost_teleport_distance': 1,
    'spacebend_teleport_distance': 1,
    'fairy_walkstyle_tms_autoadd': True,
    'fairy_teleport_tms_autoadd': True,
    'fairy_teleport_distance': 1
}

CONFIG_CHANGE_SHOW = {
    'disable_notifs': False,
    'wellness_tms_autoadd': False,
    'vampire_bat_tms_autoadd': False,
    'vampire_mist_tms_autoadd': False,
    'vampire_run_tms_autoadd': False,
    'witch_spell_autoadd': False,
    'witch_broom_tms_autoadd': False,
    'td1_dark_apparate_tms_autoadd': False,
    'td1_mist_spell_tms_autoadd': False,
    'td1_bat_spell_tms_autoadd': False,
    'td1_run_spell_tms_autoadd': False,
    'pet_teleport_tms_autoadd': False,
    'cheat_debug_pie_menu': True,
    'vampire_bat_distance': False,
    'vampire_mist_distance': False,
    'witch_spell_distance': False,
    'witch_broom_distance': False,
    'werewolf_run_tms_autoadd': False,
    'ghost_teleport_tms_autoadd': False,
    'spacebend_teleport_tms_autoadd': False,
    'ghost_teleport_distance': False,
    'spacebend_teleport_distance': False,
    'fairy_walkstyle_tms_autoadd': True,
    'fairy_teleport_tms_autoadd': True,
    'fairy_teleport_distance': False
}
# ======================================================================================================================
