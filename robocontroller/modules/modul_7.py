import navigation

#drej 45 grader mod venstre
#kør frem til grå linje nr 2
#følg linje til markør

GREY = 50
robot.turn(-45)
while GREY.counter() <= 2
    if line_sensor.reflection() != GREY + 5
    line_sensor.reflection() = GREY +5

    break
    GREY.counter() = 3
navigation.followline()
#tjek reflektion 
    #hvis sidste farve ikke er ny farve
    #sidste farve er ny farve
    #gråcounter ++
