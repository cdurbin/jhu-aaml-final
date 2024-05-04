import numpy as np

class RandomAgent:
    """
    An agent that always selects an action randomly, does not attempt to learn.
    """
    def __init__(self, num_actions=2):
        self.num_actions = num_actions
        self.actions = list(range(self.num_actions))

    def select_action(self, state):
        """Always choose a random action."""
        rng = np.random.default_rng()
        idx = rng.integers(low=0, high=self.num_actions)
        return idx

    def learn(self, state, action, new_state, reward, game_end):
        """Random agent does not learn."""
        pass

class FixedAgent:
    """
    An agent that always selects the same action, does not attempt to learn.
    """
    def __init__(self, num_actions=2, fixed_action=0):
        self.num_actions = num_actions
        self.actions = list(range(self.num_actions))
        self.fixed_action = fixed_action

    def select_action(self, state):
        """Always choose the same action."""
        return self.fixed_action

    def learn(self, state, action, new_state, reward, game_end):
        """Fixed agent does not learn."""
        pass
