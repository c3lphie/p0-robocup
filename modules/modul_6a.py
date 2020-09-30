#!/usr/bin/env pybricks-micropython
from .navigation import WallE
from pybricks.tools import wait

robot = WallE()


def follow_line_slow():
    can_drive = True
    while can_drive:
        # Beregn afvigelse
        deviation = robot.line_sensor.reflection() - self.threshold

        # Beregn turn_rate baseret på afvigelsen
        turn_rate = robot.PROPORTIONAL_GAIN * deviation

        # Kør robot
        robot.drive(75, turn_rate)

        # Tjekker om værdien for farvesensoren er inden for range
        if robot.line_sensor.reflection() in range(robot.WHITE - 5, robot.WHITE + 5):
            robot.stop()
            can_drive = False


def run_module():
    robot.turn(-70)
    robot.straight(100)
    robot.seek_line_straight()
    wait(10)
    robot.turn(-60)
    robot.follow_line()

    robot.straight(100)
    robot.follow_line_slow()

    robot.seek_line("left")
    robot.follow_line()
