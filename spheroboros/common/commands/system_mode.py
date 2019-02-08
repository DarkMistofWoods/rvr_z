#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x12-system_modes.json
# Device ID:          0x12
# Device Name:        system_mode
# Timestamp:          02/08/2019 @ 01:01:54.902376 (UTC)

from enum import IntEnum


class CommandsEnum(IntEnum):
    enable_play_mode_change_notify = 0x02
    set_play_mode = 0x26
    get_play_mode = 0x27
