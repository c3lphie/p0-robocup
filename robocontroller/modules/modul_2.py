#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import navigation

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Objects:
EV3=EV3Brick()
Colorsenor=farvesensor

#Code:
reset_angle(0)
run_target(100,45,then=Stop.HOLD, wait=True)
robot.straight(100)
navigation.seek_line("right")
navigation.follow_line()

