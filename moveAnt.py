from ax12.movement import sit, stand, rotate, flip, walk, connect
import time
from ax12 import Ax12


def main():
    servos = connect()

    sit(servos)
    time.sleep(1)
    stand(servos)
    time.sleep(1)
    # flip(servos)
    rotate(servos)
    # time.sleep(1)
    # walk(servos)
    # sit(servos)

    Ax12.disconnect()


if __name__ == "__main__":
    main()
