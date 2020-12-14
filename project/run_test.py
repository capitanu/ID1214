from environment import Environment
from snake_agent import Agent
import numpy as np
import time
from tensorflow.keras.models import load_model
import pygame

ENV_WIDTH = 500
ENV_ROWS = 5
episodes = 10
env = Environment(ENV_WIDTH, ENV_WIDTH, ENV_ROWS, ENV_ROWS)
agent = Agent(env)
agent.dqn_local.dqn = load_model("saved/snake_dqn.h5")


for episode in range(episodes):
    state = env.reset()
    env.render()

    while True:
        action = agent.act(state)
        print(action)
        state, reward, done, score = env.step(action)
        time.sleep(0.01)
        env.render()

        if done:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_q]:
                    exit(0)
                    

