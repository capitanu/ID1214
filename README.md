# Snake AI
# Current Version 1.0

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

## Training on top of an already trained data
1. If you have trained your snake atleast once and wish to train it again on top of that you need to include `agent.dqn_local.dqn = load_model("saved/file_name.h5")` in `qlearn.py`.
  
  Note that by default the training data will be saved every 100 episodes to `saved/snake_dqn_2.h5`

## Running
To test the snake you need to run `qtest.py` by using the following command:
```
python qtest.py
```
