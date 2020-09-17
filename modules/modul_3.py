#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()
# drejer 45 grader mod venstre


def run_module():
    robot.turn(-45)
    robot.straight(100)
    robot.seek_line_straight()
    robot.turn(45)
    robot.follow_line()
