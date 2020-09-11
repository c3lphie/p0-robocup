import navigation

robot = WallE()
# drejer 45 grader mod venstre
robot.turn(-45)

# kør til grå streg rammes
while robot.line_sensor.reflection() == GREY
    robot.drive(100)
    if robot.line_sensor.reflection() > GREY
    robot.brake()

#følg linje til markør
navigation.seek_line("left")
navigation.follow_line()