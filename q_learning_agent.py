import numpy as np

class QLearningAgent:
    def __init__(self, alpha=0.1, epsilon=0.2, gamma=0.9):
        self.num_states = 203 + 1
        self.num_actions = 2
        self.state = None
        self.action = None
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.q = np.zeros((self.num_states, self.num_actions), dtype="float32")
        self.sa_visits = np.zeros((self.num_states, self.num_actions), dtype="int")

    # Public API
    def get_number_of_states(self):
        return self.num_states

    def get_number_of_actions(self):
        return self.num_actions

    def select_action(self, state):
        print(f'State is {state}')
        self.state = state
        q_values = self.q[state, ]
        action = self.e_greedy(q_values)
        self.action = action

        self.sa_visits[state][action] += 1

        return action

    def learn(self, new_state, reward, game_end):
        """Update the q value using the Q-learning algorithm."""
        next_state_q_values = self.q[new_state, ]
        max_q = np.max(next_state_q_values)
        current_q = self.q[self.state][self.action]
        # The equation
        new_q_value = current_q + self.alpha * (reward + (self.gamma * max_q) - current_q)
        self.q[self.state][self.action] = new_q_value
        if game_end:
            self.action = None
            self.state = None
        else:
            self.state = new_state

    # def get_num_state_action_pairs_visited(self, pre_gold):
    #     state_action_visits = self.sa_visits[:64] if pre_gold else self.sa_visits[64:]
    #     return np.count_nonzero(state_action_visits)

    # def get_percent_state_action_pairs_visited(self, pre_gold):
    #     visited_sa_count = self.get_num_state_action_pairs_visited(pre_gold)
    #     total_sa_count = self.num_visitable_sa_pre_gold if pre_gold else self.num_visitable_sa_post_gold
    #     return (visited_sa_count / total_sa_count) * 100

    # Private API
    def e_greedy(self, q_values):
        """Implements epsilon greedy algorithm."""
        rng = np.random.default_rng()
        if self.epsilon <= rng.random():
            best_action_idx = np.argmax(q_values)
            return best_action_idx
        else:
            num_actions = q_values.size
            idx = rng.integers(low=0, high=num_actions)
            return idx
