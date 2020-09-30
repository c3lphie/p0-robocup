#!/usr/bin/env pybricks-micropython
from .navigation import WallE

robot = WallE()

# drej 45 grader mod venstre
# kør frem til grå linje nr 2
# følg linje til markø
def run_module():
    GREYcount = 0
    max_lines = 3
    SIDSTEFARVE = 1
    robot.straight(150)
    robot.turn(-45)
    

    while GREYcount < 3:
        robot.drive(robot.DRIVE_SPEED, 0)
        if robot.line_sensor.reflection() in range(robot.GREY - 10, robot.GREY + 10):
            if SIDSTEFARVE == 1:
                GREYcount += 1
                SIDSTEFARVE = 0 
                print(GREYcount)
        else:
            SIDSTEFARVE = 1


    robot.straight(100)
    robot.turn(45)        
    robot.follow_line()

# tjek reflektion
# hvis sidste farve ikke er ny farve
# sidste farve er ny farve
# gråcounter ++

# Lydeffekt: "I love cocaine!" https://youtu.be/Y4q_Tx3lAQA?t=51
