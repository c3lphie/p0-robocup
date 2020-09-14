#!/usr/bin/env pybricks-micropython
import navigation
from pybricks.tools import wait

robot = WallE()
radius = 5000


def check_exit():
    can_drive = True
    while can_drive:
        deviation = robot.line_sensor.reflection() - robot.threshold

        turn_rate = robot.PROPERTIONAL_GAIN * deviation

        robot.drive(100, turn_rate)
        wait(100)
        robot.stop()
        robot.turn(-90)
        if robot.light_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
            can_drive = False
            robot.follow_line()

    return


def find_flask():
    can_drive = True
    while can_drive:
        robot.turn(-90)
        if robot.ultra_sensor.distance() <= radius + 10:
            robot.stop()
            can_drive = False
            return


def run_module():
    robot.turn(-45)
    can_drive = True
    while can_drive:
        robot.drive(100)
        if robot.line_sensor.reflection() <= robot.GREY:
            robot.follow_line()
            robot.drive(100)
            if robot.line_sensor.reflection() <= robot.WHITE:
                robot.stop()

        robot.straight(radius)
        find_flask()
        robot.open_claw()
        robot.reset()
        robot.drive()
        if robot.ultra_sensor.distance() == 50:
            robot.stop()
            robot.close_claw()

        robot.straight((-1) * radius)
        robot.open_claw()
        robot.straight((-1) * radius)

        robot.turn(-360)
        if line_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
            robot.stop()
            robot.close_claw()

        check_exit()
    return


# drej 45 grader mod venstre
# kør frem til grå
# følg linje til markør
# Kør til centrum
# drej mod flaske
# kør frem til tryk sensor rammes
# luk klo
# bak til centrum
# åben klo
# bak til stor grå linje
# følg linje venstre om
# tjek til venstre i et interval
# når hovedlinje findes kør frem til markør

# Musikønske: Dead Or Alive - You Spin Me Round (Like A Record) mens robotten drejer 720 grader.
