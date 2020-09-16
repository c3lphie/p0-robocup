#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    # Drej 10 grader venstre
    robot.turn(-10)
    # kør indtil grå linje rammes
    robot.seek_line("straight")
    # tilføj in range til linereflection
    # følg linje til markør
