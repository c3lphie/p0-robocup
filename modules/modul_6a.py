#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():
    robot.straight(50)
    robot.follow_lineR2L()
