from environment import Environment
from snake_agent import Agent
import numpy as np
import time
from tensorflow.keras.models import load_model
import pygame

ENV_WIDTH = 500
ENV_ROWS = 10
episodes = 100
env = Environment(ENV_WIDTH, ENV_WIDTH, ENV_ROWS, ENV_ROWS)
agent = Agent()
agent.dqn_local.dqn = load_model("saved/snake_dqn_2.h5")

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

for episode in range(episodes):
    state = env.reset()
    env.render(state)
    moves = 0
    while True:
        action = agent.act(state)
        state, reward, done, score, apple_eaten, info = env.step(action, moves)
        time.sleep(0.01)
        env.render(state)

        if done:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_q]:
                    exit(0)
                    

