#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
robot = WallE()


def run_module():
    # Drej 20 grader venstre
    robot.turn(-10)
    robot.straight(100)
    # kør indtil grå linje rammes
    robot.seek_line_straight()
    wait(100)
    robot.turn(-100)
    wait(100)
    robot.follow_line()
    # tilføj in range til linereflection
    # følg linje til markør
