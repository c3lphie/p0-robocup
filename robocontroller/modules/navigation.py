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
    # Init sensors
    line_sensor = ColorSensor(Port.S1)
    touch_sensor = TouchSensor(Port.S2)
    ultra_sensor = UltrasonicSensor(Port.S3)
    gyro_sensor = GyroSensor(Port.S4)

    # Init motors
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    front_motor = Motor(Port.C)

    # Constants
    wheel_diameter = 47.56
    axle_track = 100
    BLACK = 3
    WHITE = 31
    GREY = 18
    DRIVE_SPEED = 100
    PROPERTIONAL_GAIN = 1.2

    threshold = (BLACK + WHITE + GREY) / 3

    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

    def __init__():
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)

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

    def open_claw():
        front_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=50)
        return

    def close_claw():
        front_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=50)
        return
