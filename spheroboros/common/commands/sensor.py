#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x18-sensors.json
# Device ID:          0x18
# Device Name:        sensor
# Timestamp:          02/08/2019 @ 01:01:54.898320 (UTC)

from enum import IntEnum


__all__ = ['CliffDetectionSensorLocationsBitMask',
           'GyroMaxFlagsBitMask',
           'InfraredSensorLocationsBitMask',
           'InfraredSensorTestDetailsFlagsBitMask']


class CommandsEnum(IntEnum):
    set_sensor_streaming_mask = 0x00
    get_sensor_streaming_mask = 0x01
    sensor_streaming_data_notify = 0x02
    get_encoder_counts = 0x09
    get_euler_angles = 0x0A
    get_gyro_degrees_per_second = 0x0B
    set_extended_sensor_streaming_mask = 0x0C
    get_extended_sensor_streaming_mask = 0x0D
    get_rightsideupness = 0x0E
    enable_gyro_max_notify = 0x0F
    gyro_max_notify = 0x10
    get_bot_to_bot_infrared_readings = 0x22
    magnetometer_calibrate_to_north = 0x25
    magnetometer_north_yaw_notify = 0x26
    start_robot_to_robot_infrared_broadcasting = 0x27
    start_robot_to_robot_infrared_following = 0x28
    stop_robot_to_robot_infrared_broadcasting = 0x29
    send_robot_to_robot_infrared_message = 0x2A
    listen_for_robot_to_robot_infrared_message = 0x2B
    robot_to_robot_infrared_message_received_notify = 0x2C
    get_magnetometer_chip_id = 0x2D
    run_infrared_self_test = 0x2E
    infrared_self_test_results_notify = 0x2F


class CliffDetectionSensorLocationsBitMask(IntEnum):
    ''' '''
    front_left = 1 #: 
    front_right = 2 #: 
    back_left = 4 #: 
    back_right = 8 #: 


class GyroMaxFlagsBitMask(IntEnum):
    ''' '''
    max_plus_x = 1 #: 
    max_minus_x = 2 #: 
    max_plus_y = 4 #: 
    max_minus_y = 8 #: 
    max_plus_z = 16 #: 
    max_minus_z = 32 #: 


class InfraredSensorLocationsBitMask(IntEnum):
    ''' '''
    front_left = 1 #: 
    front_right = 2 #: 
    back_right = 4 #: 
    back_left = 8 #: 


class InfraredSensorTestDetailsFlagsBitMask(IntEnum):
    ''' '''
    success = 1 #: 
    front_left_receiver_emitter_failed = 2 #: 
    front_right_receiver_emitter_failed = 4 #: 
    back_right_receiver_emitter_failed = 8 #: 
    back_left_receiver_emitter_failed = 16 #: 
