#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x12-system_modes.json
# Device ID:          0x12
# Device Name:        system_mode
# Timestamp:          02/08/2019 @ 01:01:54.902243 (UTC)

from spheroboros.common.commands.system_mode import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


async def enable_play_mode_change_notify(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_mode,
        CommandsEnum.enable_play_mode_change_notify,
        target,
        timeout,
        outputs=[
            Parameter(
                name='identifier',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


async def set_play_mode(self, identifier, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_mode,
        CommandsEnum.set_play_mode,
        target,
        timeout,
        inputs=[
            Parameter(
                name='identifier',
                data_type='uint16_t',
                index=0,
                value=identifier,
                size=1
            ),
        ],
    )


async def get_play_mode(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_mode,
        CommandsEnum.get_play_mode,
        target,
        timeout,
        outputs=[
            Parameter(
                name='identifier',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
        ],
    )
