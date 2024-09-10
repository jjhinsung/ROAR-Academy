## This is course material for Introduction to Modern Artificial Intelligence
## Example code: cartpole_dqn.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020-2024. Intelligent Racing Inc. Not permitted for commercial use

# Please make sure to install openAI gym module
# pip install gym==0.17.3
# pip install pyglet==1.5.29

import random
import gym
import os
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam


#PID controller constants
Kp = 1.0 # Proportional 
Ki = 0 #Integral
Kd = 0.5  #derivative


        # if e % 10 == 0:
        #     agent.save("./save/cartpole-dqn.h5")
