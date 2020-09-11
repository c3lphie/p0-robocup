import navigation

#Drej 45 grader mod højre
robot.turn(45)
#Kør til grå streg rammes
robot.straight(200)
navigation.seek_line("left")
#Åben klo
navigation.open_claw()
#Følg linje til tryk sensor rammes
while robot.ultra_sensor.distance(silent=True)
    robot.drive(DRIVE_SPEED, turn_rate)
    if robot.ultra_sensor.distance() == 50
        robot.stop
#luk klo
navigation.close_claw()
#Kør frem til markør
while line_sensor.reflection() >= BLACK + 5:
       robot.drive(DRIVE_SPEED, turn_rate)
    if line_sensor.reflection() <= BLACK + 5:
       robot.stop()
      can_drive = False