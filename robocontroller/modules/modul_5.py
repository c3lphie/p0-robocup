
from navigation import WallE
robot = WallE()

drive = True
drive2 = False
drive3 = False

# Åben klo
while drive:
    robot.open_claw()
    robot.wait(5000)
    drive2 = True
    drive = False

# Bak til grå linje og drej 135 grader mod venstre
while drive2:
   if line_sensor.reflection() <= robot.GREY + 5:
        robot.drive(-500)
    else:
        robot.turn(-135)
        wait(10000)
        drive3 = True
        drive2 = False

# Kør frem til grå linje og følg linje til markør
while drive3:
   if line_sensor.reflection() in range(robot.GREY - 5, robot.GREY + 5):
        robot.drive(500)
    elif line_sensor.reflection() <= robot.BLACK + 5:
       drive3 = False
    else:
        robot.follow_line()

# Lydeffekt: Stjerne fra Mario