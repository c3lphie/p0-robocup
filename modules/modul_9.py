#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():
    # Drej 20 grader venstre
    robot.turn(-20)
    robot.straight(150)
    # kør indtil grå linje rammes
    # robot.seek_line_straight()
    # robot.turn(-150)
    robot.follow_line()
    # tilføj in range til linereflection
    # følg linje til markør
