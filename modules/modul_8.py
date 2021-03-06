#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
robot = WallE()


def run_module():
    # Kør frem til cirkel fra modul start
    robot.close_claw()
    robot.turn(-45)
    robot.straight(200)
    robot.seek_line("left")
    robot.follow_line()

    # Kør til centrum
    radius = 500
    robot.straight(radius)

    # Sæt flaske
    robot.open_claw()

    # Bak til grå
    robot.straight(-radius)

    robot.turn(180)
    robot.follow_line()

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
