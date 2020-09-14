#!/usr/bin/env pybricks-micropython
from navigation import WallE

robot = WallE()
# drejer 45 grader mod venstre


def run_module():
    robot.turn(-45)

    # kør til grå streg rammes
    while robot.line_sensor.reflection() == robot.GREY:
        robot.drive(100)
        if robot.line_sensor.reflection() > robot.GREY:
            robot.stop()

    # følg linje til markør
    robot.seek_line("left")
    robot.follow_line()
