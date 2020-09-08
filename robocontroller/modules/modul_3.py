import navigation
#Drej 45 grader mod venstre
robot.turn(45)
#kør til grå streg rammes
robot.straight(200)
#Følg linje til makør
navigation.seek_line("left")
navigation.follow_line()