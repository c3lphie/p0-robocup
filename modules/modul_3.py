#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()
# drejer 45 grader mod venstre


def run_module():
    robot.turn(-45)
    robot.seek_line("straight")
