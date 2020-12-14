from collections import deque
import numpy as np
import random

class ReplayMemory:

    def __init__(self, dqn):
        self.replay_memory = deque(maxlen = int(1e5))
        self.batch_size = dqn.BATCH_SIZE

    def __len__(self):
        return len(self.replay_memory)

    def memorize(self, state, action, reward, next_state, done):
        self.replay_memory.append(tuple((state, action, reward, next_state, done)))

    def sample(self, INPUT_NODES):
        experiences = random.sample(self.replay_memory, k = self.batch_size)
        states, actions, rewards, next_states, dones = zip(*experiences)
        states = np.array(states).reshape(self.batch_size, INPUT_NODES)
        actions = np.array(actions, dtype = 'int').reshape(self.batch_size)
        rewards = np.array(rewards).reshape(self.batch_size)
        next_states = np.array(next_states).reshape(self.batch_size, INPUT_NODES)
        dones = np.array(dones).reshape(self.batch_size)
        return states, actions, rewards, next_states, dones

        
