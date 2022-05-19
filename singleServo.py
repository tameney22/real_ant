"""
Author: Yoseph Tamene

Short script to display a TKinter window to control the AX-12A's speed and position.

Inspired by: https://www.youtube.com/watch?v=c92E_YC9uZQ

"""


from Ax12 import Ax12
import tkinter as tk


def main(motor: Ax12):

    print("CURRENT SPEED:", motor.get_present_speed())
    window = tk.Tk()
    window.geometry("400x150")
    window.title("AX-12A Manual Control")

    # Goal Position

    goalSlider = tk.Scale(window,
                          from_=0, to=1023, orient=tk.HORIZONTAL, length=350, command=lambda v: motor.set_goal_position(int(v)))
    goalSlider.set(motor.get_goal_position())
    goalLabel = tk.Label(text="Goal Position")

    # Speed

    speedSlider = tk.Scale(window,
                           from_=0, to=1023, orient=tk.HORIZONTAL, length=350, command=lambda v: motor.set_moving_speed(int(v)))
    speedSlider.set(motor.get_moving_speed())

    speedLabel = tk.Label(text="Servo Speed")
    goalSlider.pack()
    goalLabel.pack()
    speedSlider.pack()
    speedLabel.pack()

    window.mainloop()


if __name__ == "__main__":
    Ax12.DEVICENAME = 'COM15'

    Ax12.BAUDRATE = 1_000_000

    # sets baudrate and opens com port
    Ax12.connect()
    my_dxl = Ax12(1)

    main(my_dxl)
