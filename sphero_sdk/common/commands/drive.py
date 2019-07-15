#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x16-driving.json
# Device ID:          0x16
# Device Name:        drive
# Timestamp:          07/02/2019 @ 22:49:01.158508 (UTC)

from sphero_sdk.common.enums.drive_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter


def raw_motors(left_mode, left_speed, right_mode, right_speed, target, timeout):
    return {
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.raw_motors,
        'target': target,
        'timeout': timeout,
        'inputs': [
            Parameter(
                name='leftMode',
                data_type='uint8_t',
                index=0,
                value=left_mode,
                size=1
            ),
            Parameter(
                name='leftSpeed',
                data_type='uint8_t',
                index=1,
                value=left_speed,
                size=1
            ),
            Parameter(
                name='rightMode',
                data_type='uint8_t',
                index=2,
                value=right_mode,
                size=1
            ),
            Parameter(
                name='rightSpeed',
                data_type='uint8_t',
                index=3,
                value=right_speed,
                size=1
            ),
        ],
    }


def reset_yaw(target, timeout):
    return {
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.reset_yaw,
        'target': target,
        'timeout': timeout,
    }


def drive_with_heading(speed, heading, flags, target, timeout):
    return {
        'did': DevicesEnum.drive,
        'cid': CommandsEnum.drive_with_heading,
        'target': target,
        'timeout': timeout,
        'inputs': [
            Parameter(
                name='speed',
                data_type='uint8_t',
                index=0,
                value=speed,
                size=1
            ),
            Parameter(
                name='heading',
                data_type='int16_t',
                index=1,
                value=heading,
                size=1
            ),
            Parameter(
                name='flags',
                data_type='uint8_t',
                index=2,
                value=flags,
                size=1
            ),
        ],
    }
