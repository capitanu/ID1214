import tensorflow as tf

class DQN:

    def __init__(self):
        self.BATCH_SIZE = 40
        self.GAMMA = 0.95
        self.UPDATE_RATE = 5
        self.LEARN_RATE = 0.01
        self.INPUT_NODES = 32
        self.HIDDEN_NODES = (20, 16, 10)
        self.OUTPUT_NODES = 4
        self.dqn = tf.keras.Sequential()
        self.dqn.add(tf.keras.layers.Dense(units = self.HIDDEN_NODES[0], input_dim = self.INPUT_NODES, activation = tf.nn.relu))
        self.dqn.add(tf.keras.layers.Dense(units = self.HIDDEN_NODES[1], activation = tf.nn.relu))
        self.dqn.add(tf.keras.layers.Dense(units = self.HIDDEN_NODES[2], activation = tf.nn.relu))
        self.dqn.add(tf.keras.layers.Dense(units = self.OUTPUT_NODES, activation = tf.keras.activations.linear))
        # adam = tf.keras.optimizers.Adam(self.LEARN_RATE)
        # loss_fn = tf.keras.losses.MeanSquaredError()
        # accuracy = tf.keras.metrics.Accuracy(name="accuracy", dtype=None)
        # self.dqn.compile(optimizer = adam, loss = loss_fn, metrics = accuracy)
        self.dqn.compile(optimizer = tf.keras.optimizers.Adam(self.LEARN_RATE), loss='mse',metrics=['accuracy'])

    def predict(self, state):
        return self.dqn.predict(state, self.BATCH_SIZE)

    def train(self, states, action_values):
        self.dqn.fit(states, action_values, batch_size=self.BATCH_SIZE,verbose=0, epochs=1)
