#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    # drejer 45 grader mod højre
    robot.turn(45)

    # køre 15 cm frem
    robot.distance(150)

    # drejer 90+ grader mod venstre
    robot.turn(-100)

    # køre frem til grå linje findes og følger den frem til markøren

    robot.seek_line("straight")