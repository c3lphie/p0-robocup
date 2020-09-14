#!/usr/bin/env pybricks-micropython
from navigation import WallE

robot = WallE()


class module_9:
    def run_module():
        # Drej 10 grader venstre
        robot.turn(-10)
        # kør indtil grå linje rammes
        while robot.line_sensor.reflection() > GREY + 10:
            robot.drive(100)
            if line_sensor.reflektion() == GREY:
                break

        robot.follow_line()
        # tilføj in range til linereflection
        # følg linje til markør
