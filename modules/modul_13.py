#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
robot = WallE()


def run_module():
    # kør frem til hvid rammes
    robot.straight(100)

    # mål afstand til væg
    # Afstand = robot.ultra_sensor.distance()

    # del afstand med to
    # Afstand_stop = Afstand / 2

    # kør frem til afstands måler viser forrige svar
    can_drive = True
    while can_drive:
        # Beregn afvigelse
        deviation = robot.line_sensor.reflection() - robot.threshold

        # Beregn turn_rate baseret på afvigelsen
        turn_rate = -robot.PROPORTIONAL_GAIN * deviation

        # Kør robot
        robot.drive(robot.DRIVE_SPEED, turn_rate)

        # Tjekker om værdien for farvesensoren er inden for range
        if robot.ultra_sensor.distance() <= 1350:
            robot.stop()
            can_drive = False

    # stop
    # Afspil we are the champions
    ev3.speaker.play_file("music.wav")
    wait(5000)
