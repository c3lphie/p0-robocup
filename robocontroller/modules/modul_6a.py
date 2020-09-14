#!/usr/bin/env pybricks-micropython
from navigation import WallE

robot = WallE()
class module_6a:
    def get_speed_by_angle(angle):
        speed = angle * angle * 0.2 + 1
        return speed


    def run_module():
        robot.turn(-45)
        follow_line()

        can_drive = True
        while can_drive:
        robot.drive(get_speed_by_angle(robot.gyro_sensor.angle()))
        if robot.line_sensor.reflection() >= WHITE:
            robot.stop()
            can_drive = False

        robot.seek_line("left")
