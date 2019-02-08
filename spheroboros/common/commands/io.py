#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x1A-user_io.json
# Device ID:          0x1A
# Device Name:        io
# Timestamp:          02/08/2019 @ 00:55:35.165648 (UTC)

from enum import IntEnum


__all__ = ['AudioPlaybackModesEnum',
           'SpecdrumsColorPaletteIndiciesEnum']


class CommandsEnum(IntEnum):
    set_all_leds = 0x0E
    set_all_leds_with_32_bit_mask = 0x1A
    set_all_leds_with_64_bit_mask = 0x1B
    set_all_leds_with_8_bit_mask = 0x1C


class AudioPlaybackModesEnum(IntEnum):
    ''' '''
    play_immediately = 0  #: 
    play_only_if_not_playing = 1  #: 
    play_after_current_sound = 2  #: 


class SpecdrumsColorPaletteIndiciesEnum(IntEnum):
    ''' '''
    default = 0  #: 
    midi = 1  #: 
