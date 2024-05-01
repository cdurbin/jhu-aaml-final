import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random
import copy

# class DQN(nn.Module):
#     def __init__(self, num_features, action_size, hidden_size):
#         super(DQN, self).__init__()
#         self.inputs = nn.Linear(num_features, hidden_size * 2)
#         self.relu = nn.ReLU()
#         self.hidden1 = nn.Linear(hidden_size * 2, hidden_size * 2)
#         self.hidden2 = nn.Linear(hidden_size * 2, hidden_size)
#         self.outputs = nn.Linear(hidden_size, action_size)

#     def forward(self, x):
#         # print(f'x is {x}')
#         # x = torch.FloatTensor(x).to(self.device)
#         x = self.relu(self.inputs(x))
#         x = self.relu(self.hidden1(x))
#         x = self.relu(self.hidden2(x))
#         return self.outputs(x)

class DQN(nn.Module):
    def __init__(self, num_features, action_size, hidden_size):
        super(DQN, self).__init__()
        self.inputs = nn.Linear(num_features, hidden_size * 2)
        self.bn1 = nn.BatchNorm1d(hidden_size * 2)  # Batch normalization layer after first linear layer
        self.relu = nn.ReLU()
        self.hidden1 = nn.Linear(hidden_size * 2, hidden_size * 2)
        self.bn2 = nn.BatchNorm1d(hidden_size * 2)  # Batch normalization layer after second linear layer
        self.hidden2 = nn.Linear(hidden_size * 2, hidden_size)
        self.bn3 = nn.BatchNorm1d(hidden_size)  # Batch normalization layer after third linear layer
        self.outputs = nn.Linear(hidden_size, action_size)

    def forward(self, x):
        x = self.inputs(x)
        x = self.bn1(x)  # Apply batch normalization
        x = self.relu(x)

        x = self.hidden1(x)
        x = self.bn2(x)  # Apply batch normalization
        x = self.relu(x)

        x = self.hidden2(x)
        x = self.bn3(x)  # Apply batch normalization
        x = self.relu(x)

        return self.outputs(x)

def state_to_inputs(state):
    if state is None:
        return [0, 0, 0, 0, 199]
    elif isinstance(state, int):
        return [0, 0, 0, 0, state]
    else:
        return [
            state['agent_total'],
            state['usable_ace'],
            state['dealer_visible_total'],
            state['dealer_ace'],
            200
        ]

class DQNAgent:
    def __init__(self):
        self.action_size=2
        self.replay_buffer_size=1000000
        self.min_replay_size=50
        self.batch_size=32
        self.gamma=0.95
        self.epsilon=0.2
        self.epsilon_min=0.01
        self.epsilon_decay=0.995
        self.learning_rate=0.001
        self.memory = deque(maxlen=self.replay_buffer_size)
        self.num_features = 5
        self.hidden_size = 12
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
        # self.device = 'cpu'
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f'Device is {self.device}')
        self.model = DQN(self.num_features, self.action_size, self.hidden_size).to(self.device)
        self.target_model = copy.deepcopy(self.model)
        self.update_target_every = 50
        self.step_count = 0
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()

    def select_action(self, state):
        state_input = state_to_inputs(state)
        state_tensor = torch.FloatTensor([state_input]).to(self.device)  # Adds batch dimension
        if np.random.rand() <= self.epsilon:
            action = random.randrange(self.action_size)
        else:
            self.model.eval()
            with torch.no_grad():
                action_values = self.model(state_tensor)
            action = np.argmax(action_values.cpu().data.numpy())
            self.model.train()
            # Uncomment to test choosing the worst action as a sanity check the network is learning
            # action = np.argmin(action_values.cpu().data.numpy())
        return action

    def replay(self):
        if len(self.memory) < self.min_replay_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)

        states = [state_to_inputs(s[0]) for s in minibatch]
        actions = [s[1] for s in minibatch]
        rewards = [s[2] for s in minibatch]
        next_states = [state_to_inputs(s[3]) for s in minibatch]

        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).unsqueeze(-1).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)

        current_q_values = self.model(states).gather(1, actions)
        next_q_values = self.target_model(next_states).max(1)[0].detach()

        target_q_values = rewards + (self.gamma * next_q_values)
        loss = self.criterion(current_q_values.squeeze(), target_q_values)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.step_count += 1
        if self.step_count % self.update_target_every == 0:
            self.target_model.load_state_dict(self.model.state_dict())

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def learn(self, state, action, new_state, reward, done):
        # print(f'Learn: State is {state}, new_state is {new_state}')
        self.memory.append((state, action, reward, new_state))
        self.replay()