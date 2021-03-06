#!/usr/bin/env pybricks-micropython

# ==========================================================
# This is the module used to make the robot follow the line,
# and other smart navigation related functions.
# ==========================================================

# Importing modules
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

    # CONSTANTS
    i = 5  # Konstant der bliver brugt til at skabe interval i range funktionen
    wheel_diameter = 47.56
    axle_track = 100  # Afstand mellem to aksler, i mm

    # BLACK, WHITE, GREY er definition af lysniveauet som sensoren måler
    # BLACK = 10
    # WHITE = 100
    # GREY = 48

    # Testbanens værdier
    BLACK = 8
    WHITE = 98
    GREY = 58

    # Motorens hastighed i grader per sekund
    DRIVE_SPEED = 200

    # En faktor der ganges på forskellige værdier
    PROPORTIONAL_GAIN = 2.5

    # Farve threshold
    threshold = (WHITE + GREY) / 2

    # Forklar kort
    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
    robot.settings(DRIVE_SPEED, 20, 50, 20)

    # Her sættes vores variabler ind så vi kan bruge funktionerne fra drivebase gennem vores klasse.
    def __init__(
        self,
    ):  # "self" repræsentere WallE, men så det kan bruges inde i klassen
        # "super()" er en placeholder for DriveBase klassen
        super().__init__(
            self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track
        )

    # Funktion der får robotten til at søge linjen
    def seek_line(self, direction):
        can_drive = True
        turn_int = 5
        # Først tjekkes hvad der er givet som argument
        if direction == "right":
            # Sætter robotten til at dreje mod højre
            while can_drive:
                self.robot.turn(turn_int)
                # Tjekker om værdien for farvesensoren er inden for range
                if self.line_sensor.reflection() in range(
                    self.GREY - self.i, self.GREY + self.i
                ):
                    self.robot.stop()
                    can_drive = False
                    return True
        # Tjekker om argument er lig venstre
        elif direction == "left":
            # Sætter robotten til at dreje mod venstre
            while can_drive:
                self.robot.turn(-turn_int)
                # Tjekker om værdien for farvesensoren er inden for range
                if self.line_sensor.reflection() in range(
                    self.GREY - self.i, self.GREY + self.i
                ):
                    self.robot.stop()
                    can_drive = False
                    return True
        else:
            return False

    # Funktionen der får robotten til at søge ligeud efter linjen
    def seek_line_straight(self):
        can_drive = True
        turn_rate = 0
        # Sætter robotten til at køre
        while can_drive:
            self.robot.drive(self.DRIVE_SPEED, turn_rate)
            # Tjekker om værdien for farvesensoren er inden for range
            if self.line_sensor.reflection() in range(
                self.GREY - self.i, self.GREY + self.i
            ):
                self.robot.stop()
                can_drive = False
                return

    # Funktion for at følge linjen
    def follow_line(self):
        can_drive = True
        while can_drive:
            # Beregn afvigelse
            deviation = self.line_sensor.reflection() - self.threshold

            # Beregn turn_rate baseret på afvigelsen
            turn_rate = self.PROPORTIONAL_GAIN * deviation

            # Kør robot
            self.robot.drive(self.DRIVE_SPEED, turn_rate)

            # Tjekker om værdien for farvesensoren er inden for range
            if self.line_sensor.reflection() in range(self.BLACK - 5, self.BLACK + 5):
                self.robot.stop()
                can_drive = False
        return

    # Funktionen for at følge linjen fra venstre
    def follow_lineR2L(self):
        can_drive = True
        while can_drive:
            # Beregn afvigelse
            deviation = self.line_sensor.reflection() - self.threshold

            # Beregn turn_rate baseret på afvigelsen
            turn_rate = -self.PROPORTIONAL_GAIN * deviation

            # Kør robot
            self.robot.drive(self.DRIVE_SPEED, turn_rate)

            # Tjekker om værdien for farvesensoren er inden for range
            if self.line_sensor.reflection() in range(self.BLACK - 5, self.BLACK + 5):
                self.robot.stop()
                can_drive = False
        return

    def open_claw(self):
        self.front_motor.run_until_stalled(-600, then=Stop.HOLD, duty_limit=55)
        return

    def close_claw(self):
        self.front_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=65)
        return
