from navigation import WallE

robot = WallE()

# kør frem til hvid rammes
while robot.line_sensor.reflection() != robot.WHITE - 5:
    robot.reset()
    robot.drive(500)

# mål afstand til væg
Afstand = robot.ultra_sensor.distance()

# del afstand med to
Afstand_stop = Afstand / 2


# kør frem til afstands måler viser forrige svar
move = True

while move:
    Distance_measured = robot.distance()
    if Distance_measured == Afstand_stop:
        robot.stop()
        move = False
    else:
        robot.drive()


# stop
# Afspil we are the champions
ev3.speaker.play_file("music.wav")
wait(5000)
