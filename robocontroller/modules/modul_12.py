from navigation import WallE

robot = WallE()

# drejer 45 grader mod højre
robot.turn(45)

# køre 15 cm frem
robot.distance(150)

# drejer 90+ grader mod venstre
robot.turn(-100)

# køre frem til grå linje findes og følger den frem til markøren

move = True

while move:
    if robot.line_sensor.reflection() <= GREY + 5:
        robot.stop()
        move = False
    else:
        robot.follow_line()
