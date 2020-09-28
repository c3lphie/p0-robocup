#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def get_speed_by_angle(angle):
    speed = angle * angle * -0.02 + 75
    return speed


def run_module():
    # robot.turn(-60)
    # robot.seek_line_straight()
    # wait(10)
    # robot.turn(-60)
    # robot.follow_line()

    robot.close_claw()

    # can_drive = True
    # while can_drive:
    #     angle = robot.gyro_sensor.angle()
    #     robot.drive(get_speed_by_angle(angle),0)
    #     if robot.line_sensor.reflection() >= robot.WHITE:
    #         robot.stop()
    #         can_drive = False

    robot.follow_line()
    if robot.line_sensor.reflection() in range(robot.WHITE - 5, robot.WHITE + 5):
        robot.stop()

    robot.seek_line("left")
    robot.follow_line()
