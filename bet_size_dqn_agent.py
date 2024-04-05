import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random
from dqn_agent import DQN

def state_to_inputs(state):
    # print(state)
    return list(state.values())
    # return [state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8], state[9], state[10]]

class BetSizeDQNAgent:
    def __init__(self):
        self.action_size=2
        self.replay_buffer_size=2000
        self.min_replay_size=50
        self.batch_size=32
        self.gamma=0.95
        self.epsilon=0.2
        self.epsilon_min=0.01
        self.epsilon_decay=0.995
        self.learning_rate=0.001
        self.memory = deque(maxlen=self.replay_buffer_size)
        self.num_features = 10
        self.hidden_size = 32
        self.model = DQN(self.num_features, self.action_size, self.hidden_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()
        self.device = 'cpu'

    def select_action(self, state):
        state_input = state_to_inputs(state)
        state_tensor = torch.FloatTensor([state_input]).to(torch.device(self.device))  # Adds batch dimension
        if np.random.rand() <= self.epsilon:
            action = random.randrange(self.action_size)
        else:
            self.model.eval()
            with torch.no_grad():
                action_values = self.model(state_tensor)
            action = np.argmax(action_values.cpu().data.numpy())
            # Uncomment to test choosing the worst action as a sanity check the network is learning
            # action = np.argmin(action_values.cpu().data.numpy())
        return action

    def replay(self):
        if len(self.memory) < self.min_replay_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state in minibatch:
            state_input = torch.FloatTensor([state_to_inputs(state)]).to(torch.device(self.device))
            next_state_input = torch.FloatTensor([state_to_inputs(next_state)]).to(torch.device(self.device))
            reward = torch.FloatTensor([reward]).to(torch.device(self.device))
            action = torch.LongTensor([action]).to(torch.device(self.device))

            Q_expected = self.model(state_input).gather(1, action.unsqueeze(-1)).squeeze(-1)
            Q_next = self.model(next_state_input).max(1)[0].detach()
            Q_target = reward + (self.gamma * Q_next)

            loss = self.criterion(Q_expected, Q_target)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def learn(self, state, action, new_state, reward, done):
        # print(f'Learn: State is {state}, new_state is {new_state}')
        self.memory.append((state, action, reward, new_state))
        self.replay()