#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    # drejer 45 grader mod højre
    robot.turn(60)
    robot.close_claw()
    # køre 15 cm frem
    robot.straight(650)

    # drejer 90+ grader mod venstre
    robot.turn(-170)

    # køre frem til grå linje findes og følger den frem til markøren

    robot.seek_line_straight()
    robot.straight(70)
    robot.turn(50)
    robot.open_claw()
    robot.PROPORTIONAL_GAIN = 3
    robot.follow_line()
