#!/usr/bin/env python3
# This file is automatically generated!
# Toy Name:           Sphero RVR
# Prefix:             RV
# Timestamp:          07/02/2019 @ 21:20:31.358406 (UTC)

from enum import IntEnum


class SpheroRvrTargets(IntEnum):
    ''' '''
    Primary = 1  #:
    Secondary = 2  #:


class SpheroRvrLedBitMasks(IntEnum):
    ''' '''
    left_status_indication_red = 0x00000001  #:
    left_status_indication_green = 0x00000002  #:
    left_status_indication_blue = 0x00000004  #:
    right_status_indication_red = 0x00000008  #:
    right_status_indication_green = 0x00000010  #:
    right_status_indication_blue = 0x00000020  #:
    left_headlight_red = 0x00000040  #:
    left_headlight_green = 0x00000080  #:
    left_headlight_blue = 0x00000100  #:
    right_headlight_red = 0x00000200  #:
    right_headlight_green = 0x00000400  #:
    right_headlight_blue = 0x00000800  #:
    door_1_red = 0x00001000  #:
    door_1_green = 0x00002000  #:
    door_1_blue = 0x00004000  #:
    door_2_red = 0x00008000  #:
    door_2_green = 0x00010000  #:
    door_2_blue = 0x00020000  #:
    side_1_red = 0x00040000  #:
    side_1_green = 0x00080000  #:
    side_1_blue = 0x00100000  #:
    side_2_red = 0x00200000  #:
    side_2_green = 0x00400000  #:
    side_2_blue = 0x00800000  #:
    rear_1_red = 0x01000000  #:
    rear_1_green = 0x02000000  #:
    rear_1_blue = 0x04000000  #:
    rear_2_red = 0x08000000  #:
    rear_2_green = 0x10000000  #:
    rear_2_blue = 0x20000000  #:
    undercarriage_white = 0x40000000  #:
