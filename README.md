# Snake AI

## Dependencies
There exists four dependencies:

1. numpy
2. tensorflow
3. tkinter
4. pygame


To install dependencies, run `pip3 install -r requirements.txt`

## Getting started

1. Clone the repo or download it in some way `git clone https://github.com/capitanu/ID1214.git`
2. In order to train the snake you need to run `qlearn.py`by using the following command:
```
python qlearn.py
```
3. To change the settings of the training such as number of training episodes and number of rows you need to change `episodes` and `ENV_ROWS` variables in `qlearn.py`.
4. Enjoy! 

## Running
To test the snake you need to run `qtest.py` by using the following command:
```
python qtest.py
```

## Settings

Some variables that you might want to change in order to tweak the training or the running of the snake:

### Running

In **qtest.py** :

	ENV_ROWS = X

Where X is the number of rows you'd want your snake's environemnt to be.

	agent.dqn_local.dqn = load_model("saved/7x7.h5")
	
Where you could replace **7x7.h5** with one of the trained networks located under __saved/__.


### Learning

In **qlearn.py** :

	ENV_ROWS = X
	
Where X is the number of rows you would want your snake's environment to be.

	episodes = X

Where X is the number of games you want the agent to play.

	GROW = X
	
Where X is the number of episodes you want the snake to run on the same size map. If you want the size to be constant, make sure that **GROW** is larger than **episodes**.

