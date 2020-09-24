#!/usr/bin/env pybricks-micropython

# ==========================================================
# This is the module used to make the robot follow the line,
# and other smart navigation related functions.
# ==========================================================
from pybricks.ev3devices import (
    Motor,
    ColorSensor,
    TouchSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase


class WallE(DriveBase):
    # Init sensors
    line_sensor = ColorSensor(Port.S1)
    ultra_sensor = UltrasonicSensor(Port.S3)
    gyro_sensor = GyroSensor(Port.S4)

    # Init motors
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    front_motor = Motor(Port.C)

    # Constants
    i = 5   # Konstant der bliver brugt til at skabe interval i range funktionen
    wheel_diameter = 47.56 
    axle_track = 100    # Afstand mellem to aksler, i mm

    # BLACK, WHITE, GREY er definition af lysniveauet som sensoren måler
    BLACK = 6   
    WHITE = 91
    GREY = 55

    # Motorens hastighed i grader per sekund
    DRIVE_SPEED = 150

    # En faktor der ganges på forskellige værdier
    PROPORTIONAL_GAIN = 1.2     
    PROPORTIONAL_GAIN2 = -1.2

    # Farve threshold
    threshold = (WHITE + GREY) / 2 

    # Forklar kort
    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track) 

    # Få Simon til at forklare super, self. Initialisering af motor
    def __init__(self): # Få Simon til at forklare (self), forklaring af classes
        super().__init__(
            self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track
        )

    # Funktion der får robotten til at søge linjen - få lige en gennemgang af Simon
    def seek_line(self, direction):
        if direction == "right": 
            self.robot.turn(360)
            if self.line_sensor.reflection() in range(
                self.GREY - self.i, self.GREY + self.i
            ):
                self.robot.stop()
                return True
    
        elif direction == "left":
            self.robot.turn(-360)
            if self.line_sensor.reflection() in range(
                self.GREY - self.i, self.GREY + self.i
            ):
                self.robot.stop()
                return True
        else:
            return False

    def seek_line_straight(self):
        can_drive = True
        turn_rate = 0
        while can_drive:
            self.robot.drive(self.DRIVE_SPEED, turn_rate)
            if self.line_sensor.reflection() in range(
                self.GREY - self.i, self.GREY + self.i
            ):
                self.robot.stop()
                can_drive = False
                return

    def follow_line(self):
        can_drive = True
        while can_drive:
            deviation = self.line_sensor.reflection() - self.threshold

            turn_rate = self.PROPORTIONAL_GAIN * deviation

            self.robot.drive(self.DRIVE_SPEED, turn_rate)

            if self.line_sensor.reflection() in range(self.BLACK - 5, self.BLACK + 5):
                self.robot.stop()
                can_drive = False
        return

    def follow_lineR2L(self):
        can_drive = True
        while can_drive:
            deviation = self.line_sensor.reflection() - self.threshold

            turn_rate = self.PROPORTIONAL_GAIN2 * deviation

            self.robot.drive(self.DRIVE_SPEED, turn_rate)

            if self.line_sensor.reflection() in range(self.BLACK - 5, self.BLACK + 5):
                self.robot.stop()
                can_drive = False
        return

    def open_claw(self):
        self.front_motor.run_until_stalled(-300, then=Stop.HOLD, duty_limit=70)
        return

    def close_claw(self):
        self.front_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=70)
        return
