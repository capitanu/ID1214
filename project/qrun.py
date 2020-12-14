from environment import Environment
from snake_agent import Agent
import tensorflow as tf
import numpy as np
import time
import keyboard
import pygame

ENV_WIDTH = 500
ENV_ROWS = 5
#night episodes = 10000000000
episodes = 10000
epsilon, eps_min, eps_decay = 1, 0.05, 0.9997
env = Environment(ENV_WIDTH, ENV_WIDTH, ENV_ROWS, ENV_ROWS)
agent = Agent(env)
best_score = 0
score = 0
for episode in range(1, episodes + 1):

    epsilon = max(epsilon*eps_decay, eps_min)
    state = env.reset()    
    action = agent.act(state, epsilon)
    
    env.render()

    score = 0

    while True:
        next_state, reward, done, score = env.step(action)
        agent.experience(state, action, reward, next_state, done)
        agent.learn()
        env.render()

        if done:
            break

        state = next_state
        action = agent.act(state, epsilon)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_q]:
                    agent.save()
                    exit(0)
agent.save()
