import numpy as np

class QLearningAgent:
    def __init__(self, alpha=0.1, epsilon=0.002, gamma=0.9):
        self.num_states = 203 + 1
        self.num_actions = 2
        self.actions = list(range(self.num_actions))
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.q = {}

    # Public API
    def get_number_of_states(self):
        return self.num_states

    def get_number_of_actions(self):
        return self.num_actions

    def select_action(self, state):
        # print(f'State is {state}')
        q_values = []
        for action in self.actions:
            key = self.get_state_action_pair_key(state, action)
            q_value = self.q.get(key, 0)
            q_values.append(q_value)
        action = self.e_greedy(q_values)

        return action

    def get_state_action_pair_key(self, state, action):
        if isinstance(state, int):
            return (state,action)
        state_tuple = (state['agent_total'], state['usable_ace'], state['dealer_visible_total'], state['dealer_ace'], action)
        return state_tuple

    def get_max_q_value(self, state):
        q_values = []
        for action in self.actions:
            key = self.get_state_action_pair_key(state, action)
            q_value = self.q.get(key, 0)
            q_values.append(q_value)
        return np.max(q_values)

    def learn(self, state, action, new_state, reward, game_end):
        """Update the q value using the Q-learning algorithm."""
        max_q = self.get_max_q_value(new_state)
        key = self.get_state_action_pair_key(state, action)
        current_q = self.q.get(key, 0)
        new_q_value = current_q + self.alpha * (reward + (self.gamma * max_q) - current_q)
        self.q[key] = new_q_value


    # Private API
    def e_greedy(self, q_values):
        """Implements epsilon greedy algorithm."""
        rng = np.random.default_rng()
        if self.epsilon <= rng.random():
            best_action_idx = np.argmax(q_values)
            return best_action_idx
        else:
            num_actions = len(q_values)
            idx = rng.integers(low=0, high=num_actions)
            return idx
