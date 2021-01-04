from environment import Environment
from snake_agent import Agent
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
import time
import pygame



ENV_WIDTH = 500
ENV_ROWS = 5
#night episodes = 10000000000
episodes = 150000
wall = 0
itself = 0
ate = 0
won = 0
stuck = 0
each = 0


epsilon, eps_min, eps_decay = 0.9, 0.05, 0.9997
env = Environment(ENV_WIDTH, ENV_WIDTH, ENV_ROWS, ENV_ROWS)
agent = Agent()
#agent.dqn_local.dqn = load_model("saved/calin_1.h5")

def print_data(score, max_score, info, episode):
    global wall
    global itself
    global ate
    global won
    global stuck
    print("Max score: " + str(max_score))
    print("Episode: " + str(episode))
    print("Hit the wall: " + str(wall))
    print("Hit itself: " + str(itself))
    print("Ate the food: " + str(ate))
    print("Stuck: " + str(stuck))
        
    print("THERE IS NO WAY IT WON: " + str(won))
    
    print("--------------------")
    print("--------------------")
        
        
        
    
max_score = 0
#while(True):
for episode in range(1, episodes + 1):
    each += 1
    epsilon = max(epsilon*eps_decay, eps_min)
    
    state = env.reset()
    env.render(state)
    action = agent.act(state, epsilon)
   
    moves = 0
    info = 0
    apple_eaten = False
    while True:
        next_state, reward, done, score, apple_eaten, info = env.step(action, moves)
        if apple_eaten:
            moves = 0
        agent.experience(state, action, reward, next_state, done)
        agent.learn()
        
        moves += 1
        if(each % 10 == 0):
            print_data(score, max_score, info, episode)
            each += 1
        if(each % 100 == 0):
            agent.save()
        if(score > max_score):
            max_score = score
        if(info == 1):
            wall = wall + 1

        if(info == 4):
            won = won + 1

        if(info == 5):
            stuck = stuck + 1
        if(info == 2):
            itself = itself + 1

        if(info == 3):
            ate = ate + 1
            
        if done:
            break
        state = next_state
        env.render(state)
        
        action = agent.act(state, epsilon)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_q]:
                    agent.save()
                    exit(0)

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")      
agent.save()
