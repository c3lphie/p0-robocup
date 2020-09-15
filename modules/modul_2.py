#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    reset_angle(0)
    robot.turn(45)
    robot.straight(100)
    robot.seek_line("right")
    robot.follow_line()