#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():
    robot.reset()
    robot.turn(60)
    robot.straight(100)
    robot.seek_line_straight()
    robot.turn(-60)
    robot.follow_line()
