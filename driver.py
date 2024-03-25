import monte_carlo_agent
import q_learning_agent
import blackjack_env

import numpy as np
import os
import sys

# Usage: `python Project2_main.py` to run the assignment as specified
# To run a different test scenario (described below) run `python Project2_main.py <scenario number>`
def main(scenario=1):
    """
    There are three ways to run my code controlled by the passed in scenario number (1, 2, or 3).
    1. Scenario 1: Run the test as specified by the assignment and capture the required metrics.
    2. Scenario 2: Run additional training episodes to attempt to converge and then run a loop
    at the end that only exploits to see win rates for optimal play.
    3. Scenario 3: Run each agent until it has visited every state and track the number of episodes
    required for each agent.
    """
    print(f'Running scenario {scenario}')
    NUM_EPISODES = 2000
    if scenario == 2:
        NUM_EPISODES = 10000
    NUM_AGENTS = 10
    agents_win_rates = []
    agents_win_rates_excluding_ties = []
    agents_cumulative_rewards = []
    # agents_percent_states_visited = []
    episodes_required = []
    for a in range(NUM_AGENTS):
        agents_win_rates.append([])
        agents_win_rates_excluding_ties.append([])
        agents_cumulative_rewards.append([])
        # agents_percent_states_visited.append([])
        environment = blackjack_env.Blackjack()
        # agent = monte_carlo_agent.RlAgent()
        agent = q_learning_agent.QLearningAgent()
        wins = 0
        ties = 0
        cumulative_rewards = 0
        if scenario == 3:
            # i = 0
            # while agent.get_num_states_visited() < agent.get_number_of_states() - 1:
            #     i = i + 1
            #     current_state = environment.reset()
            #     game_end = False
            #     while not game_end:
            #         action = agent.select_action(current_state)
            #         new_state, reward, game_end = environment.execute_action(action)
            #         cumulative_rewards += reward
            #         agent.update_q(new_state, reward, game_end)
            #         current_state = new_state
            # episodes_required.append(i)
            print(f"There is no scenario 3")
        else:
            for i in range(NUM_EPISODES):
                # reset the game and observe the current state
                current_state = environment.reset()
                game_end = False
                # Do until the game ends:
                while not game_end:
                    action = agent.select_action(current_state)
                    # print(f'Action selected is {action}')
                    new_state, reward, game_end = environment.execute_action(action)
                    cumulative_rewards += reward
                    agent.update_q(new_state, reward, game_end)
                    current_state = new_state
                    if game_end:
                        if reward > 0:
                            wins += 1
                        elif reward == 0:
                            ties += 1
                        if scenario == 1:
                            agents_win_rates[a].append(wins / (i + 1.0))
                            agents_win_rates_excluding_ties[a].append(wins / max([1, (i + 1.0 - ties)]))
                            agents_cumulative_rewards[a].append(cumulative_rewards)
                            # agents_percent_states_visited[a].append(agent.get_percent_states_visited())
            if scenario == 1:
                print(f"Agent {a} Win rate: {wins / (NUM_EPISODES):.2f}, Win rate excluding ties: {wins / (NUM_EPISODES - ties):.2f}")
                print(f"Agent {a} Wins: {wins}, losses: {(NUM_EPISODES - ties - wins)}, ties: {ties}")
                # print(f"Agent {a} Number of states visited: {agent.get_num_states_visited()}, Percent states visited: {agent.get_percent_states_visited():.1f}\n")

        # Exploit only
        if scenario == 2:
            wins = 0
            ties = 0
            agent.epsilon = 0.0
            for i in range(NUM_EPISODES):
                current_state = environment.reset()
                game_end = False
                while not game_end:
                    action = agent.select_action(current_state)
                    new_state, reward, game_end = environment.execute_action(action)
                    agent.update_q(new_state, reward, game_end)
                    current_state = new_state
                    if game_end:
                        if reward > 0:
                            wins += 1
                        elif reward == 0:
                            ties += 1
                        agents_win_rates[a].append(wins / (i + 1.0))
                        agents_win_rates_excluding_ties[a].append(wins / max([1, (i + 1.0 - ties)]))
                        agents_cumulative_rewards[a].append(cumulative_rewards)
                        # agents_percent_states_visited[a].append(agent.get_percent_states_visited())
            print(f"Agent {a} win rate while exploiting and excluding ties: {wins / (NUM_EPISODES - ties):.2f}")
            print(f"Agent {a} wins: {wins}, losses: {(NUM_EPISODES - ties - wins)}, ties: {ties}\n")
    if scenario == 1 or scenario == 2:
        avg_win_rate = np.mean(agents_win_rates, axis=0)
        avg_win_rate_no_ties = np.mean(agents_win_rates_excluding_ties, axis=0)
        print(f'Mean win rate: {avg_win_rate[-1]:.2f}, Mean win rate excluding ties: {avg_win_rate_no_ties[-1]:.2f}')
    if scenario == 1:
        avg_cumulative_rewards = np.mean(agents_cumulative_rewards, axis=0)
        # avg_percent_state_visited = np.mean(agents_percent_states_visited, axis=0)
        print(f'Mean cumulative rewards: {avg_cumulative_rewards[-1]:.1f}')
        # print(f'Mean percent states visited: {avg_percent_state_visited[-1]:.2f}')
    elif scenario == 3:
        print(episodes_required)
        print(f'Mean number of episodes required: {int(np.mean(episodes_required))}')

    # Save off the files to use for analysis and generating charts
    os.makedirs('output', exist_ok=True)
    np.save('output/agents_win_rates', agents_win_rates)
    np.save('output/agents_cumulative_rewards', agents_cumulative_rewards)
    # np.save('output/agents_percent_states_visited', agents_percent_states_visited)
    print("Program completed successfully.")

if __name__ == "__main__":
    scenario = 1
    if len(sys.argv) >= 2:
        try:
            scenario = int(sys.argv[1])
            if scenario != 1 and scenario != 2 and scenario != 3:
                print(f"The passed in scenario number {scenario} is invalid, it must be 1, 2, or 3.")
                exit(1)
        except:
            print("The passed in scenario must be an integer: 1, 2, or 3.")
            exit(1)

    main(scenario)
