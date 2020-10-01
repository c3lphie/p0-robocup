#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():
    robot.straight(200)
    robot.follow_line()
