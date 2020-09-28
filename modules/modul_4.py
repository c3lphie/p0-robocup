#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
robot = WallE()


def run_module():
    robot.open_claw()
    # Drej 45 grader mod højre
    robot.turn(45)
    # Kør til grå streg rammes
    robot.straight(50)
    robot.seek_line_straight()
    while robot.ultra_sensor.distance()>=400:
        robot.turn(5)
    robot.stop
    robot.turn(35)
    robot.DRIVE_SPEED = 100
    # robot.follow_lineR2L()
    # # Åben klo
    # Følg linje til tryk sensor rammes
    can_drive = True
    while can_drive:
        robot.drive(robot.DRIVE_SPEED, 0)
        if robot.ultra_sensor.distance() <= 75:
            robot.stop()
            can_drive = False
    # luk klo
    robot.close_claw()
    robot.straight(100)
    robot.turn(10)
    # Spil Celine Dion "Titanic"

    # Kør frem til markør
    while robot.line_sensor.reflection() >= robot.BLACK + 5:
        robot.drive(robot.DRIVE_SPEED, 0)
        if robot.line_sensor.reflection() in range(robot.BLACK - 5, robot.BLACK + 5):
            robot.stop()
            can_drive = False
    robot.stop()
    robot.open_claw()
