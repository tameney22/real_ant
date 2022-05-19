from ax_12.Ax12 import Ax12


MOVING_SPEED = 300


def main(motor: Ax12):
    goal = None
    while True:
        if goal == None:
            goal = input("Enter a goal position (0-1023) or q to quit: ")
            if goal == "q":
                break

            goal = int(goal)
            print("Moving to", goal)
            motor.set_moving_speed(MOVING_SPEED)
        else:
            curr_pos = motor.get_present_position()
            print("Current Position:", curr_pos)

            if curr_pos == goal:
                motor.set_moving_speed(0)
                goal = None


if __name__ == "__main__":
    Ax12.DEVICENAME = 'COM15'
    Ax12.BAUDRATE = 1_000_000

    # sets baudrate and opens com port
    Ax12.connect()

    my_dxl = Ax12(1)
    my_dxl.set_moving_speed(0)

    main(my_dxl)
