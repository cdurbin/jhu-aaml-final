import monte_carlo_agent
import q_learning_agent
import blackjack_env
import dqn_agent
import bet_size_dqn_agent

import numpy as np
import os
import sys

BET_SIZE = {0: 10, 1: 500}

# Usage: `python driver.py` to run the assignment as specified
# To run a different test scenario (described below) run `python driver.py <scenario number>`
def main(scenario=1, agent_type=1):
    print(f'Running scenario {scenario}')
    # NUM_EPISODES = 2000
    # NUM_AGENTS = 10
    NUM_EPISODES = 400000
    NUM_AGENTS = 1
    agents_win_rates = []
    agents_win_rates_excluding_ties = []
    agents_cumulative_rewards = []
    agents_balance = []
    agents_bet_sizes = []
    if agent_type == 1:
        print('Using Monte Carlo agent')
    elif agent_type == 2:
        print('Using Q-learning agent')
    else:
        print('Using DQN agent')
    for a in range(NUM_AGENTS):
        agents_win_rates.append([])
        agents_win_rates_excluding_ties.append([])
        agents_cumulative_rewards.append([])
        agents_balance.append([])
        agents_bet_sizes.append([])
        environment = blackjack_env.Blackjack()
        if agent_type == 1:
            agent = monte_carlo_agent.RlAgent()
        elif agent_type == 2:
            agent = q_learning_agent.QLearningAgent()
        else:
            agent = dqn_agent.DQNAgent()
        bet_agent = bet_size_dqn_agent.BetSizeDQNAgent()
        wins = 0
        ties = 0
        cumulative_rewards = 0
        agent_balance = 0
        for i in range(NUM_EPISODES):
            if (i % 1000 == 0):
                print(f'Starting episode {i + 1}')
            # reset the game and observe the current state
            deck_state = environment.reset()

            # TODO take the deck state and pass it in to the bet agent to get the bet
            current_bet = bet_agent.select_action(deck_state)

            # If current_bet is 0 I expect to lose and if current_bet is 1 I expect to win
            current_state = environment.deal_hand()
            bet_reward = 0
            game_end = False
            if current_state == 303:
                bet_reward = 1.5
                if current_bet == 0:
                    bet_reward = -1.5
                game_end = True
            elif current_state == 202:
                bet_reward = 0
                game_end = True

            # Do until the game ends:
            while not game_end:
                action = agent.select_action(current_state)
                # print(f'Action selected is {action}')
                new_state, reward, game_end = environment.execute_action(action)
                cumulative_rewards += reward
                agent.learn(current_state, action, new_state, reward, game_end)
                current_state = new_state
                if game_end:
                    if reward > 0:
                        wins += 1
                        agent_balance += BET_SIZE[current_bet]
                    elif reward == 0:
                        ties += 1
                    else:
                        agent_balance -= BET_SIZE[current_bet]
                    # Update the bet size agent model
                    bet_reward = reward
                    if current_bet == 0: # Small size bet - expected to lose
                        bet_reward = -1 * bet_reward # Reward a loss and punish a win

            opposite_bet = 0
            if current_bet == 0:
                opposite_bet = 1

            bet_agent.learn(deck_state, current_bet, deck_state, bet_reward, True)
            bet_agent.learn(deck_state, opposite_bet, deck_state, -bet_reward, True)

            if scenario == 1:
                agents_win_rates[a].append(wins / (i + 1.0))
                agents_win_rates_excluding_ties[a].append(wins / max([1, (i + 1.0 - ties)]))
                agents_cumulative_rewards[a].append(cumulative_rewards)
                agents_balance[a].append(agent_balance)
                agents_bet_sizes[a].append(BET_SIZE[current_bet])


        if scenario == 1:
            print(f"Agent {a} Win rate: {wins / (NUM_EPISODES):.2f}, Win rate excluding ties: {wins / (NUM_EPISODES - ties):.2f}")
            print(f"Agent {a} Wins: {wins}, losses: {(NUM_EPISODES - ties - wins)}, ties: {ties}")
            print(f'Agent {a} Final balance: {agent_balance}')

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
                    agent.learn(new_state, reward, game_end)
                    current_state = new_state
                    if game_end:
                        if reward > 0:
                            wins += 1
                        elif reward == 0:
                            ties += 1
                        agents_win_rates[a].append(wins / (i + 1.0))
                        agents_win_rates_excluding_ties[a].append(wins / max([1, (i + 1.0 - ties)]))
                        agents_cumulative_rewards[a].append(cumulative_rewards)
            print(f"Agent {a} win rate while exploiting and excluding ties: {wins / (NUM_EPISODES - ties):.2f}")
            print(f"Agent {a} wins: {wins}, losses: {(NUM_EPISODES - ties - wins)}, ties: {ties}\n")
            print(f'Agent {a} Final balance: {agents_balance}')

    if scenario == 1 or scenario == 2:
        avg_win_rate = np.mean(agents_win_rates, axis=0)
        avg_win_rate_no_ties = np.mean(agents_win_rates_excluding_ties, axis=0)
        print(f'Mean win rate: {avg_win_rate[-1]:.2f}, Mean win rate excluding ties: {avg_win_rate_no_ties[-1]:.2f}')
    if scenario == 1:
        avg_cumulative_rewards = np.mean(agents_cumulative_rewards, axis=0)
        print(f'Mean cumulative rewards: {avg_cumulative_rewards[-1]:.1f}')

    # Save off the files to use for analysis and generating charts
    os.makedirs('output', exist_ok=True)
    np.save('output/agents_win_rates', agents_win_rates)
    np.save('output/agents_cumulative_rewards', agents_cumulative_rewards)
    np.save('output/agents_balance', agents_balance)
    np.save('output/agents_bet_sizes', agents_bet_sizes)

    print("Program completed successfully.")

if __name__ == "__main__":
    scenario = 1
    if len(sys.argv) >= 2:
        try:
            scenario = int(sys.argv[1])
            if scenario != 1 and scenario != 2:
                print(f"The passed in scenario number {scenario} is invalid, it must be 1 or 2.")
                exit(1)
        except:
            print("The passed in scenario must be an integer: 1 or 2.")
            exit(1)

    agent_type = 2
    main(scenario, agent_type)