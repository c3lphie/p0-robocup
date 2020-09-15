#!/usr/bin/env pybricks-micropython
from .navigation import WallE


def run_module_1():
    robot = WallE()
    # Robotten skal følge linje til markør
    robot.line_follow()


# musik valg: https://www.youtube.com/watch?v=9Gc4QTqslN4
