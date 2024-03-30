import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random

class DQN(nn.Module):
    def __init__(self, num_features, action_size, hidden_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(num_features, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, action_size)

    def forward(self, x):
        # print(f'x is {x}')
        x = torch.FloatTensor(x)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        return self.fc3(x)

def state_to_inputs(state):

    if state is None:
        return [0, 0, 0, 0, 199]
    elif isinstance(state, int):
        return [0, 0, 0, 0, state]
    else:
        return [state['agent_total'], state['usable_ace'], state['dealer_visible_total'], state['dealer_ace'], 200]

class DQNAgent:
    def __init__(self, action_size=2, replay_buffer_size=2000, min_replay_size=50,
                 batch_size=32, gamma=0.95, epsilon=0.2, epsilon_min=0.01, epsilon_decay=0.995, learning_rate=0.001):
        self.action_size = action_size
        self.memory = deque(maxlen=replay_buffer_size)
        self.min_replay_size = min_replay_size
        self.batch_size = batch_size
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        num_features = 5
        hidden_size = 24
        self.model = DQN(num_features, action_size, hidden_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.criterion = nn.MSELoss()
        self.action = None
        self.state = None

    # def select_action(self, state):
    #     # state = torch.FloatTensor(state).unsqueeze(0)
    #     self.state = state
    #     print(f'Select action: State is {state}')
    #     if np.random.rand() <= self.epsilon:
    #         action = random.randrange(self.action_size)
    #         self.action = action
    #         return action
    #     self.model.eval()
    #     with torch.no_grad():
    #         action_values = self.model(state)
    #     self.model.train()
    #     action = np.argmax(action_values.cpu().data.numpy())
    #     self.action = action
    #     print(f'Selected action is {action}')
    #     return action
    def select_action(self, state):
        state_input = state_to_inputs(state)
        state_tensor = torch.FloatTensor([state_input]).to(torch.device("cpu"))  # Adds batch dimension
        if np.random.rand() <= self.epsilon:
            action = random.randrange(self.action_size)
        else:
            self.model.eval()
            with torch.no_grad():
                action_values = self.model(state_tensor)
            action = np.argmax(action_values.cpu().data.numpy())
            # action = np.argmin(action_values.cpu().data.numpy())
        self.action = action
        return action
        # return np.argmax(action_values.cpu().data.numpy())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self):
        if len(self.memory) < self.min_replay_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in minibatch:
            state_input = torch.FloatTensor([state_to_inputs(state)]).to(torch.device("cpu"))
            next_state_input = torch.FloatTensor([state_to_inputs(next_state)]).to(torch.device("cpu"))
            reward = torch.FloatTensor([reward]).to(torch.device("cpu"))
            action = torch.LongTensor([action]).to(torch.device("cpu"))
            done = torch.FloatTensor([done]).to(torch.device("cpu"))

            Q_expected = self.model(state_input).gather(1, action.unsqueeze(-1)).squeeze(-1)
            Q_next = self.model(next_state_input).max(1)[0].detach()
            Q_target = reward + (self.gamma * Q_next * (1 - done))

            loss = self.criterion(Q_expected, Q_target)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        # for state, action, reward, next_state, done in minibatch:
        #     # state = torch.FloatTensor(state).unsqueeze(0)
        #     # next_state = torch.FloatTensor(next_state).unsqueeze(0)
        #     state = torch.FloatTensor(state)
        #     next_state = torch.FloatTensor(next_state)
        #     reward = torch.FloatTensor([reward])
        #     action = torch.LongTensor([action])
        #     done = torch.FloatTensor([done])

        #     Q_expected = self.model(state_to_inputs(state)).gather(1, action.unsqueeze(1)).squeeze(1)
        #     Q_next = self.model(state_to_inputs(state)).max(1)[0].detach()
        #     Q_target = reward + (self.gamma * Q_next * (1 - done))

        #     loss = self.criterion(Q_expected, Q_target)
        #     self.optimizer.zero_grad()
        #     loss.backward()
        #     self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def learn(self, new_state, reward, game_end):
        # print(f'Learn: State is {self.state}, new_state is {new_state}')
        self.remember(self.state, self.action, reward, new_state, game_end)
        self.replay()
        self.state = new_state
        if game_end:
            self.state = None