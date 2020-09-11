import navigation

#drej 45 grader mod venstre
#kør frem til grå linje nr 2
#følg linje til markør

GREY = 18
GREYcount = 0
SIDSTEFARVE = line_sensor.reflection()
robot.turn(-45)
while GREYcount <= 3:
    if SIDSTEFARVE != GREY + 5:
        SIDSTEFARVE = line_sensor.reflection()
        GREYcount +=1
navigation.followline()
#tjek reflektion 
    #hvis sidste farve ikke er ny farve
    #sidste farve er ny farve
    #gråcounter ++

# Lydeffekt: "I love cocaine!" https://youtu.be/Y4q_Tx3lAQA?t=51