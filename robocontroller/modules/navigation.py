#!/usr/bin/env pybricks-micropython

# ==========================================================
# This is the module used to make the robot follow the line,
# and other smart navigation related functions.
# ==========================================================
from pybricks.ev3devices import (
    Motor,
    ColorSensor,
    TouchSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


class WallE(DriveBase):
    wheel_diameter = 47.56
    axle_track = 100

    BLACK = 3
    WHITE = 31
    GREY = 18

    threshold = (BLACK + WHITE + GREY) / 3

    DRIVE_SPEED = 100

    PROPERTIONAL_GAIN = 1.2

    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

    def __init__(
        self,
        left_motor,
        right_motor,
        middle_motor,
    ):
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.middle_motor = middle_motor

        self.line_sensor = line_sensor
        self.touch_sensor = touch_sensor
        self.ultra_sensor = ultra_sensor
        self.gyro_sensor = gyro_sensor

    def seek_line(direction):
        if direction == "right":
            robot.turn(360)
            if line_sensor.reflection() <= GREY + 5:
                robot.stop()
                follow_line()

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
