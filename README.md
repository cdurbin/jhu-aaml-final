# Deep Reinforcement Learning Final Project

## Pre-requisites
In order to run you will need all of the libraries in the requirements.txt file installed.
```
pip install -r requirements.txt
```

## Usage
The project supports several different types of agents to be used for choosing actions for playing Blackjack hands and optionally for selecting bet sizes. For a full list of capabilities and defaults you can run the following to print out the usage:

```
python driver.py --help
```

## Notebooks
There is a notebook that was used for generating charts. It uses files from prior run outputs to generate the charts. I left it fully executed to show what was used in the final paper.

## Running DQN bet size agent and DQN playing hands agent from the paper
```
python driver.py -e 1000000 -t dqn -b dqn -a 10
```
This will execute 10 runs with one million episodes in each run utilizing a DQN agent for playing hands and a DQN agent for selecting the bet sizes.
Note that this test took more than 30 hours on my machine and is not sped up when using a GPU. Every 5000 episodes it will generate charts in the output directory that can be used to monitor the progress and performance so far.
