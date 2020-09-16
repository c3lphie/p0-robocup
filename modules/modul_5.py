#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():
    drive2 = True
    drive3 = False
    robot.open_claw()

    # Bak til grå linje og drej 135 grader mod venstre
    while drive2:
        if line_sensor.reflection() >= robot.GREY + 5:
            robot.drive(-300)
        else:
            robot.turn(-135)
            drive3 = True
            drive2 = False

    # Kør frem til grå linje og følg linje til markør
    while drive3:
        if line_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
            robot.drive(300)
        elif line_sensor.reflection() <= robot.BLACK + 5:
            drive3 = False
        else:
            robot.follow_line()

    # Lydeffekt: Stjerne fra Mario
