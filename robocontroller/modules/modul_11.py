import navigation

# køre frem til 10 cm til mur
robot.straight(150)

# drejer 45 grader mod venstre
robot.turn(-45)

# måler afstanden til muren og bevæger sig frem til 10 cm før muren.
move = True

while = move:
    if ultra_sensor.distance() <= 100 :
        robot.run(200)
        move = False
robot.stop()


# robotten drejer 90 grader mod højre og køre 30 cm frem.
        
robot.turn(90)
robot.straight(300)

# drejer 90 grader mod venstre, søger efter grå linje og følger den.

robot.turn(-90)

move2 = True

while = move2:
    if line_sensor.reflection() <= GREY + 5:
        robot.run(200)
        move2 = False
    else navigation.follow_line

# Spil "Ronald Reagan speech - Mr. Gorbachev, tear down that wall" når robotten kører over muren
# https://youtu.be/GCO9BYCGNeY?t=112