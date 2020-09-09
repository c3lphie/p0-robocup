#!/usr/bin/env pybricks-micropython
import navigation
from pybricks.parameters import Port

robot = WallE(Port.A,Port.B,Port.C)


def get_speed_by_angle(angle):
    speed = angle * angle * 0.2 + 1
    return speed


def run_module():
    robot.turn(-45)
    follow_line()

    can_drive = True
    while can_drive:
    robot.drive(get_speed_by_angle())
    if line_sensor.reflection() >= WHITE:
        robot.stop()
        can_drive = False
        seek_line("left")
