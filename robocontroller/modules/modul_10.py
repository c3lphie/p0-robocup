# drej 45 grader mod venstre
# kør frem til grå
# drej 90 grader mod højre
# kør frem til grå linje rammes
# følg linje til markør

from navigation import WallE
robot = WallE()

# Start med at dreje -45 grader for at vende mod tredje moduls gråstreg
robot.turn(-45)
robot.wait(5000)

# Robotten kører ligeud indtil farven under den skifter til grå og drejer derefter 90 grader den anden vej
drive10 = True
drive10_2 = False
while drive10 == True:
    if robot.line_sensor.reflection() <= robot.GREY + 5:
        robot.turn(90)
        robot.wait(7500)
        drive10_2 = True
        drive10 = False
    else:
        robot.drive(500)

# Kør frem til grå linje rammes


while drive10_2 == True:
    if robot.line_sensor.reflection() > robot.GREY + 10:
        robot.drive(500)
    elif robot.line_sensor.reflection() <= robot.BLACK + 5:
        drive10_2 = False
    else:
        robot.follow_line

# Følg linjen indtil den skifter til sort
robot.follow_line
