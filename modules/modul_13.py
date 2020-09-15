#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()


def run_module():
    move = True
    move = False

    # kør frem til hvid rammes
    while move:
        robot.straight(50)
        robot.reset()

    # mål afstand til væg
    Afstand = robot.ultra_sensor.distance()

    # del afstand med to
    Afstand_stop = Afstand / 2

    # kør frem til afstands måler viser forrige svar
    move2 = True

    while move:
        Distance_measured = robot.distance()
        if Distance_measured == Afstand_stop:
            robot.stop()
            move2 = False
        else:
            robot.drive()

    # stop
    # Afspil we are the champions
    ev3.speaker.play_file("music.wav")
    wait(5000)