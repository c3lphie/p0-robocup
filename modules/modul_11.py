#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    # køre frem til 10 cm til mur
    robot.open_claw()
    robot.turn(30)
    robot.straight(465)
    robot.turn(-30)

    # drejer 45 grader mod venstre
    robot.turn(-80)

    # måler afstanden til muren og bevæger sig frem til 10 cm før muren.
    move = True
    while move:
        robot.drive(robot.DRIVE_SPEED,0)
        if robot.ultra_sensor.distance() <= 150:
            move = False
    robot.stop()

    # robotten drejer 90 grader mod højre og køre 30 cm frem.

    robot.turn(150)
    robot.straight(650)

    # drejer 90 grader mod venstre, søger efter grå linje og følger den.

    robot.turn(-110)

    robot.seek_line_straight()
    robot.turn(30)
    robot.follow_lineR2L()


    # ny kode for alternativ løsning
    #robot.straight(200)
    #robot.turn(30)
    #robot.straight(400)
    #robot.turn(-100)
    #seek_line_straight

    # Spil "Ronald Reagan speech - Mr. Gorbachev, tear down that wall" når robotten kører over muren
    # https://youtu.be/GCO9BYCGNeY?t=112
