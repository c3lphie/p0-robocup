#!/usr/bin/env pybricks-micropython
from .navigation import WallE


class module_1:
    def run_module():
        robot = WallE()
        # Robotten skal følge linje til markør
        robot.follow_line()


# musik valg: https://www.youtube.com/watch?v=9Gc4QTqslN4
