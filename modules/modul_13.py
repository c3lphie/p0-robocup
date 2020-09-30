#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
robot = WallE()


def run_module():
    move = True
    move2 = False

    # kør frem til hvid rammes
    while move:
        robot.straight(500)
        robot.reset()
        move = False

    # mål afstand til væg
    #Afstand = robot.ultra_sensor.distance()

    # del afstand med to
    #Afstand_stop = Afstand / 2

    # kør frem til afstands måler viser forrige svar
    move2 = True

    while move2:
        Distance_measured = robot.distance()
        if Distance_measured == 1350:
            robot.stop()
            move2 = False
        else:
            robot.follow_line

    # stop
    # Afspil we are the champions
    ev3.speaker.play_file("music.wav")
    wait(5000)
