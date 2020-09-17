#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    robot.reset()
    robot.turn(60)
    robot.wait(2000)
    robot.seek_line("straight")
