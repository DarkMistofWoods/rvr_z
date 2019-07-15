#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x16-driving.json
# Device ID:          0x16
# Device Name:        drive
# Timestamp:          07/02/2019 @ 21:20:31.345431 (UTC)

from enum import IntEnum


__all__ = ['RawMotorModesEnum',
           'DriveFlagsBitMask']


class CommandsEnum(IntEnum):
    raw_motors = 0x01
    reset_yaw = 0x06
    drive_with_heading = 0x07


class RawMotorModesEnum(IntEnum):
    ''' '''
    off = 0  #: 
    forward = 1  #: 
    reverse = 2  #: 


class DriveFlagsBitMask(IntEnum):
    ''' '''
    drive_reverse = 1 #: 
    boost = 2 #: 
    fast_turn = 4 #: 
    left_direction = 8 #: 
    right_direction = 16 #: 
    enable_drift = 32 #: 
