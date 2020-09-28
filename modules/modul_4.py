#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
robot = WallE()


def run_module():
    # Drej 45 grader mod højre
    robot.turn(45)
    # Kør til grå streg rammes
    robot.straight(100)
    robot.turn(70)
    robot.DRIVE_SPEED = 100
    robot.follow_lineR2L()
    # Åben klo
    robot.open_claw()
    # Følg linje til tryk sensor rammes
    can_drive = True
    while can_drive:
        robot.drive()
        if robot.ultra_sensor.distance() <= 59:
            robot.stop()
            can_drive = False
    # luk klo
    robot.close_claw()

    # Spil Celine Dion "Titanic"

    # Kør frem til markør
    while robot.line_sensor.reflection() >= robot.BLACK + 5:
        robot.drive()
        if robot.line_sensor.reflection() in range(robot.BLACK - 5, robot.BLACK + 5):
            robot.stop()
            can_drive = False
