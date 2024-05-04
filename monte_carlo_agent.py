import numpy as np

def check_for_duplicates(trajectory, state, action):
    """Checks to see if there is another row in the provided trajectory for the
    same state and action. For the first visit Monte Carlo algorithm we only want
    to process the first visit."""
    for row in trajectory:
        if row['s'] == state and row['a'] == action:
            return True
    return False

class RlAgent:
    def __init__(self):
        self.num_states = 203
        self.num_actions = 2
        self.actions = list(range(self.num_actions))
        self.state = None
        self.action = None
        self.epsilon = 0.15
        self.discount_factor = 1.0
        self.current_trajectory = []
        self.q = {}
        self.sa_visits = {}

    def get_number_of_states(self):
        return self.num_states

    def get_number_of_actions(self):
        return self.num_actions

    def select_action(self, state):
        if self.state is None:
            self.current_trajectory = [{'s': state}]
        self.state = state
        q_values = []
        for action in self.actions:
            key = self.get_state_action_pair_key(state, action)
            q_value = self.q.get(key, 0)
            q_values.append(q_value)

        action = self.e_greedy(q_values)
        self.action = action
        self.current_trajectory[-1]['a'] = action
        return action

    def get_state_action_pair_key(self, state, action):
        if isinstance(state, int):
            return (state,action)
        state_tuple = (state['agent_total'], state['usable_ace'], state['dealer_visible_total'], state['dealer_ace'], action)
        return state_tuple

    def learn(self, state, action, new_state, reward, game_end):
        """Update the q value using the first visit Monte Carlo control algorithm."""
        self.current_trajectory.append({'r': reward, 's': new_state})
        if game_end:
            self.replay_trajectory()
            self.current_trajectory = []
            self.action = None
            self.state = None
        else:
            self.state = new_state

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

    def replay_trajectory(self):
        """Replays the trajectory implementing the first visit Monte Carlo algorithm."""
        trajectory = self.current_trajectory
        trajectory.reverse() # process the trajectory backwards
        G = 0
        for i in range(len(trajectory) - 1):
            reward = trajectory[i]['r']
            G = self.discount_factor * G + reward
            state = trajectory[i + 1]['s']
            action = trajectory[i + 1]['a']
            has_duplicate = False
            if i < len(trajectory) - 2:
                has_duplicate = check_for_duplicates(trajectory[i+2:], state, action)
            if not has_duplicate:
                key = self.get_state_action_pair_key(state, action)
                q = self.q.get(key, 0)
                n = self.sa_visits.get(key, 1)
                self.sa_visits[key] = n + 1
                updated_q = q + ((G - q) / n)
                self.q[key] = updated_q
