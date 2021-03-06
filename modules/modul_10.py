#!/usr/bin/env pybricks-micropython
# drej 45 grader mod venstre
# kør frem til grå
# drej 90 grader mod højre
# kør frem til grå linje rammes
# følg linje til markør

from .navigation import WallE

robot = WallE()


def run_module():
    # Start med at dreje -45 grader for at vende mod tredje moduls gråstreg
    robot.turn(-75)
    robot.straight(100)

    # Robotten kører ligeud indtil farven under den skifter til grå og drejer derefter 90 grader den anden vej
    drive10 = True
    drive10_2 = False
    while drive10:
        if robot.line_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
            robot.turn(160)
            drive10_2 = True
            drive10 = False
        else:
            robot.drive(300, 0)

    # Kør frem til grå linje rammes
    robot.straight(100)
    robot.seek_line_straight()
    robot.turn(-75)

    # Følg linjen indtil den skifter til sort
    robot.follow_line()

    # Musikønske: "Tokyo Drift" https://www.youtube.com/watch?iuJDhFRDx9M=v
