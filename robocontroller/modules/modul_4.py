import navigation
robot = WallE()

#Drej 45 grader mod højre
robot.turn(45)
#Kør til grå streg rammes
robot.straight(200)
robot.seek_line("left")
#Åben klo
robot.open_claw()
#Følg linje til tryk sensor rammes
while robot.ultra_sensor.distance(silent=True):
    robot.drive()
    if robot.ultra_sensor.distance() == 50:
        robot.stop
#luk klo
robot.close_claw()
#Kør frem til markør
while robot.line_sensor.reflection() >= BLACK + 5:
       robot.drive()
    if robot.line_sensor.reflection() <= BLACK + 5:
       robot.stop()
      can_drive = False