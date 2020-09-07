#!/usr/bin/env pybricks-micropython
import navigation
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port

gyro_sensor = GyroSensor(Port.s4)


def get_speed_by_angle(angle):
    speed = angle * angle * 0.2 + 1
    return speed


def run_module():
    robot.turn(-45)
    follow_line()
    robot.drive(get_speed_by_angle(gyro_sensor.angle()))
    if line_sensor.reflection() >= WHITE:
        robot.stop()
        seek_line("left")
