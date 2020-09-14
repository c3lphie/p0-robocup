from navigation import WallE
robot = WallE()

move = True
move = False

# kør frem til hvid rammes
while move:
    robot.straight(50)

# mål afstand til væg
Afstand = distance()

# del afstand med to
Afstand_stop = Afstand / 2


# kør frem til afstands måler viser forrige svar
move2 = True

while move2:
  Distance_measured = distance()
   if Distance_measured == Afstand_stop:
        robot.stop()
        move2 = False
    else:
        robot.follow_line_hvid


# stop
# Afspil we are the champions
ev3.speaker.play_file("music.wav")
wait(5000)
