#!/usr/bin/env pybricks-micropython

# ==========================================================
# This is the module used to make the robot follow the line,
# and other smart navigation related functions.
# ==========================================================
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Init motor
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
front_motor = Motor(Port.C)

# Init sensor
line_sensor = ColorSensor(S1)
touch_sensor = TouchSensor(S2)
ultra_sensor = UltrasonicSensor(S3)
gyro_sensor = GyroSensor(S4)




wheel_diameter = 55.5

# Init drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track=104)

# Light threshhold
BLACK = 9
WHITE = 85
GREY = 50

threshold = (BLACK + WHITE + GREY) / 3

DRIVE_SPEED = 100

PROPERTIONAL_GAIN = 1.2


def seek_line(direction):
    if direction == "right":
        robot.turn(360)
        if line_sensor.reflection() <= GREY + 5:
            robot.stop()
            follow_line()
            return True

    elif direction == "left":
        robot.turn(-360)
        if line_sensor.reflection() <= GREY + 5:
            robot.stop()
            follow_line()
            return True
    else:
        return False


def follow_line():
    can_drive = True
    while can_drive:
        deviation = line_sensor.reflection() - threshold

        turn_rate = PROPERTIONAL_GAIN * deviation

        robot.drive(DRIVE_SPEED, turn_rate)

        if line_sensor.reflection() <= BLACK + 5:
            robot.stop()
            can_drive = False
    return
