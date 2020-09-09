import navigation

#Drej 45 grader mod højre
robot.turn(45)
#Kør til grå streg rammes
robot.straight(200)
navigation.seek_line("left")
#Åben klo
#Følg linje til tryk sensor rammes
#luk klo
#Kør frem til markør