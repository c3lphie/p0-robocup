#!/usr/bin/env pybricks-micropython 
from modules import modul_1, modul_2, modul_3, modul_4, modul_5, modul_6a, modul_7, modul_8, modul_8, modul_9, modul_10, modul_11, modul_12, modul_13, navigation
from pybricks.tools import wait

wait(1000)
def run():
    #modul_1.run_module()
    #modul_2.run_module()
    #modul_3.run_module()
    #modul_4.run_module()
    #modul_5.run_module()
    #modul_6a.run_module()
    #modul_7.run_module()
    #modul_8.run_module()
    #modul_9.run_module()
    modul_10.run_module()
    modul_11.run_module()
    modul_12.run_module()
    modul_13.run_module()
    return

if __name__ == "__main__":
    run() 
    robot = navigation.WallE()

    #robot.close_claw()
    #wait(100)
    #robot.open_claw()

