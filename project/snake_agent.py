import random
from dqn import DQN
import numpy as np
from replay_memory import ReplayMemory

class Agent():

    def __init__(self, env):
        self.env = env
        
        self.dqn_local = DQN()
        self.batch_size = self.dqn_local.BATCH_SIZE

        print(self.dqn_local.dqn.summary())
        
        self.dqn_target = DQN()

        self.replay_memory = ReplayMemory(self.dqn_local)

        self.t = 0

    def learn(self):
        if self.replay_memory.__len__() > self.batch_size:
            states, actions, rewards, next_states, dones = self.replay_memory.sample(self.dqn_local.INPUT_NODES)
            target = self.dqn_local.predict(states)
            target_val = self.dqn_target.predict(next_states)
            target_next = self.dqn_local.predict(next_states)
            max_action_values = np.argmax(target_next, axis = 1)

            for i in range(self.batch_size):
                if dones[i]:
                    target[i][actions[i]] = rewards[i]
                else:
                    target[i][actions[i]] = rewards[i] + self.dqn_local.GAMMA * target_val[i][max_action_values[i]]


            self.dqn_local.train(states, target)

            if self.t == self.dqn_local.UPDATE_RATE:
                self.update_target_weights()
                self.t = 0
            else:
                self.t = self.t + 1

    def act(self, state, epsilon = 0):
        state = state.reshape((1,) + state.shape)
#        print(state)
        action_values = self.dqn_local.predict(state)
        if random.random() > epsilon:
            action = np.argmax(action_values)
        else:
            action = random.randint(0, self.dqn_local.OUTPUT_NODES - 1)
        return action

    def experience(self, state, action, reward, next_state, done):
        self.replay_memory.memorize(state, action, reward, next_state, done)

    def update_target_weights(self):
        self.dqn_target.dqn.set_weights(self.dqn_local.dqn.get_weights())

    def save(self):
        self.dqn_local.dqn.save('saved/snake_dqn_2.h5')

            
