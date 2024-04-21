import numpy as np

class RandomAgent:
    def __init__(self):
        self.num_actions = 2
        self.actions = list(range(self.num_actions))

    def get_number_of_actions(self):
        return self.num_actions

    def select_action(self, state):
        """Always choose a random action."""
        rng = np.random.default_rng()
        idx = rng.integers(low=0, high=self.num_actions)
        return idx

    def learn(self, state, action, new_state, reward, game_end):
        """Random agent does not learn."""
        pass
