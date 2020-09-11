import navigation
robot = WallE()
#Drej 10 grader venstre
robot.turn(-10)
#kør indtil grå linje rammes
while line_sensor.reflection() > GREY + 10:
    robot.drive(100)
if line_sensor.reflektion() == GREY:
    break
robot.follow_line()
#tilføj in range til linereflection
#følg linje til markør