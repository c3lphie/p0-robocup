# IMPORTANT LINKS:
GitHub: https://github.com/c3lpie/p0-robocup

Trello: https://trello.com/b/CTfQSttK/project-management

Overleaf: TBA


# Definering af motor og sensor

left_motor = Motor(Port.A)\
right_motor = Motor(Port.B)\
front_motor = Motor(Port.C)\

line_sensor = ColorSensor(S1)\
touch_sensor = TouchSensor(S2)\
ultra_sensor = UltrasonicSensor(S3)\
gyro_sensor = GyroSensor(S4)


# IMPORTANT FILES:
p0.org - pseudokode brainstorm af bane

billede.png - bane brainstorm

# Nice to have:
# - Før mur i modul_11.py, vent lidt for komedisk effekt, afspil lydfil (såsom "Move bitch, get out the way", eller et kampvogns skud, en sirene eller noget), og kravl over muren. 