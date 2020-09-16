#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    robot.reset()
    robot.turn(45)
    robot.straight(200)
    robot.seek_line("straight")
    robot.follow_line()
