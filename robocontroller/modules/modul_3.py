import navigation
#drej 45 grader mod venstre
robot.turn(45)
#kør til grå streg rammes
robot.straight(200)
#følg linje til markør
navigation.seek_line("left")
navigation.follow_line()
