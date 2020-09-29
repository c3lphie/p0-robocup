#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    # drejer 45 grader mod højre
    robot.turn(60)

    # køre 15 cm frem
    robot.straight(550)

    # drejer 90+ grader mod venstre
    robot.turn(-150)

    # køre frem til grå linje findes og følger den frem til markøren

    robot.seek_line_straight()
    robot.turn(30)
    robot.follow_line()
