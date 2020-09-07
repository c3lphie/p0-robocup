from navigation import follow_line, seek_line, follow_line_white

# kør frem til hvid rammes
while line_sensor.reflection() != WHITE - 5:
    robot.drive(500)

# mål afstand til væg
Afstand = distance()

# del afstand med to
Afstand_stop = Afstand / 2


# kør frem til afstands måler viser forrige svar
move = True

while move = True
  Distance_measured = distance()
   if Distance_measured == Afstand_stop:
        robot.stop()
        move = False
    else:
        follow_line_hvid


# stop
# Afspil we are the champions
ev3.speaker.play_file("music.wav")
wait(5000)
