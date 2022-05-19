"""
Author: Yoseph Tamene
Short script to change the ID of a given servo.
"""

from Ax12 import Ax12

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = 'COM15'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

print("=== Make sure you only have one servo connected ===")

currID = int(input("Enter the current ID: "))

toID = int(input("What ID would you like to assign: "))

my_dxl = Ax12(currID)

# Changing the id
my_dxl.set_id(toID)

if my_dxl.get_id() == 0:
    print("== Successfully changed ID! ==")
else:
    print("Something may have gone wrong. Please use the Dynamixel Wizard to check if the ID has changed.")


Ax12.disconnect()
