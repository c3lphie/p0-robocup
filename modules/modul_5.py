#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def run_module():

    drive2 = True
    drive3 = False
    robot.close_claw()

    # Bak til grå linje og drej 135 grader mod venstre
    robot.straight(-350)
    while drive2:        
        if robot.line_sensor.reflection() >= robot.GREY + 5:
            robot.turn(-230)
            drive3 = True
            drive2 = False
        else:
            robot.drive(-300, 0)
    robot.straight(100)

    # Kør frem til grå linje og følg linje til markør
    while drive3:
        if robot.line_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
            robot.turn(40)
            robot.follow_lineR2L()
        elif robot.line_sensor.reflection() <= robot.BLACK + 5:
            drive3 = False
        else:
            robot.drive(100, 0)

    # Lydeffekt: Stjerne fra Mario
