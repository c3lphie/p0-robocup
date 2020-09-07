#drej 45 grader mod venstre
#kør frem til grå
#drej 90 grader mod højre
#kør frem til grå linje rammes
#følg linje til markør

import navigation

# Start med at dreje -45 grader for at vende mod tredje moduls gråstreg
robot.turn(-45)

# Robotten kører ligeud indtil farven under den skifter til grå og drejer derefter 90 grader den anden vej
# while line_sensor.reflection() > GREY + 5
robot.drive(500)
    if: line_sensor.reflection() <= GREY + 5
        robot.turn(90)
    else: 
        robot.drive(500)

# Kør frem til grå linje rammes
# while line_sensor.reflection() > GREY + 5
     if: line_sensor.reflection() <= GREY + 5
         follow_line
     else: 
         robot.drive(500)

# Følg linjen indtil den skifter til sort
follow_line()

