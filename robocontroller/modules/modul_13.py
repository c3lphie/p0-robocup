import navigation
# kør frem til hvid rammes
while line_sensor.reflection() not <= WHITE - 5:
    robot.drive(500)

# mål afstand til væg
Afstand = distance()

# del afstand med to
Afstand_stop = Afstand / 2

# kør frem til afstands måler viser forrige svar
while True
  Distance_measured = distance()
   if Distance_measured == Afstand_stop:
        robot.stop()
    else:
        follow_line  # Hvid


# stop
# Afspil we are the champions
