#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()

# drej 45 grader mod venstre
# kør frem til grå linje nr 2
# følg linje til markø
def run_module():
    GREYcount = 0
    SIDSTEFARVE = robot.line_sensor.reflection()
    robot.turn(-45)
    while GREYcount <= 3:
        if SIDSTEFARVE != robot.GREY + 5:
            SIDSTEFARVE = robot.line_sensor.reflection()
            GREYcount += 1
            robot.drive()
    robot.follow_line()


# tjek reflektion
# hvis sidste farve ikke er ny farve
# sidste farve er ny farve
# gråcounter ++

# Lydeffekt: "I love cocaine!" https://youtu.be/Y4q_Tx3lAQA?t=51
