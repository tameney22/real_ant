import pybullet_envs
import gym
import numpy as np
from time import time
import random

env = gym.make('AntBulletEnv-v0')

# Note: Unlike ordinary gym, pybullet requires you to call render() just once, at the start
# See: https://github.com/benelot/pybullet-gym/issues/25
env.render()

env.reset()

start = time()

action = np.zeros(8)

JOINT = 0

angle = 0

print("Observation Space:", env.observation_space)

while True:

    obs, _, _, _ = env.step(action)

    # Allow a second for ant to hit the floor
    if time() - start > 1:
        # joint = int(input("Enter joint to move: "))
        # angle = float(input("Enter angle to move to: "))

        # value = np.sin(angle)

        action[1] = angle
        print("Observation:", obs[5: 13])

        angle += 20000

        # print(action)
