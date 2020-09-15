#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#!/usr/bin/env pybricks-micropython
from modules import modul_1, modul_2, modul_3, modul_4, modul_5, modul_6, modul_7, modul_8, modul_8, modul_9, modul_10, modul_11, modul_12, modul_13
#!/usr/bin/env pybricks-micropython

# ==========================================================
# This is the module used to make the robot follow the line,
# and other smart navigation related functions.
# ==========================================================

# Create your objects here.
ev3 = EV3Brick()


# class WallE(DriveBase):
    #Init sensors
    # line_sensor = ColorSensor(Port.S1)
    # ultra_sensor = UltrasonicSensor(Port.S3)
    # gyro_sensor = GyroSensor(Port.S4)
# 
    #Init motors
    # left_motor = Motor(Port.A)
    # right_motor = Motor(Port.B)
    # front_motor = Motor(Port.C)
# 
    #Constants
    # wheel_diameter = 47.56
    # axle_track = 100
    # BLACK = 6
    # WHITE = 80 
    # GREY = 46
    # DRIVE_SPEED = 100
    # PROPERTIONAL_GAIN = 1.2
# 
    # threshold = (BLACK + WHITE + GREY) / 3
    # robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
# 
    # def __init__(self):
        # super().__init__(self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track)
# 
    # def seek_line(direction):
        # if direction == "right":
            # robot.turn(360)
            # if line_sensor.reflection() <= GREY + 5:
                # robot.stop()
                # follow_line()
# 
        # elif direction == "left":
            # robot.turn(-360)
            # if line_sensor.reflection() <= GREY + 5:
                # robot.stop()
                # follow_line()
                # return True
        # else:
            # return False
# 
    # def follow_line():
        # can_drive = True
        # while can_drive:
            # deviation = line_sensor.reflection() - threshold
# 
            # turn_rate = PROPERTIONAL_GAIN * deviation
# 
            # robot.drive(DRIVE_SPEED, turn_rate)
# 
            # if line_sensor.reflection() <= BLACK + 5:
                # robot.stop()
                # can_drive = False
        # return
# 
    # def open_claw():
        # front_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=70)
        # return
# 
    # def close_claw():
        # front_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=70)
        # return
# 

# Write your program here.
ev3.speaker.beep()
wait(100)
ev3.speaker.beep()
wait(100)

def run():
    modul_1.run_module()
    modul_2.run_module()
    modul_3.run_module()
    modul_4.run_module()
    modul_5.run_module()
    modul_6a.run_module()
    modul_7.run_module()
    modul_8.run_module()
    modul_9.run_module()
    modul_10.run_module()
    modul_11.run_module()
    modul_12.run_module()
    modul_13.run_module()
    return

if __name__ == "__main__":
    run()
