#!/usr/bin/env pybricks-micropython
from .navigation import WallE



def run_module():
    robot = WallE()
    # Robotten skal følge linje til markør
    robot.straight(100)
    robot.follow_line()


# musik valg: https://www.youtube.com/watch?v=9Gc4QTqslN4
