import monte_carlo_agent
import q_learning_agent
import blackjack_env
import dqn_agent
import bet_size_dqn_agent
import random_agent

import numpy as np
import os
import sys
import argparse

BET_SIZE = {0: 10, 1: 500}

def main(scenario, agent_type, num_episodes, num_agents, use_bet_sizes):
    print(f'Running scenario {scenario} with {num_agents} {agent_type} agents and {num_episodes} episodes')
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
    for a in range(num_agents):
        agents_win_rates.append([])
        agents_win_rates_excluding_ties.append([])
        agents_cumulative_rewards.append([])
        agents_balance.append([])
        agents_bet_sizes.append([])
        environment = blackjack_env.Blackjack()
        if agent_type == 'monte-carlo':
            agent = monte_carlo_agent.RlAgent()
        elif agent_type == 'q-learning':
            agent = q_learning_agent.QLearningAgent()
        elif agent_type == 'dqn':
            agent = dqn_agent.DQNAgent()
        elif agent_type == 'random':
            agent = random_agent.RandomAgent()
        else:
            print(f'Unknown agent type {agent_type}')
            exit(1)
        bet_agent = bet_size_dqn_agent.BetSizeDQNAgent()
        wins = 0
        ties = 0
        cumulative_rewards = 0
        agent_balance = 0
        last_balance = agent_balance
        current_bet = 0
        bet_counts = {0: 0, 1: 0}
        for i in range(num_episodes):
            if (i % 1000 == 0):
                print(f'Starting episode {i + 1}')
                if use_bet_sizes:
                    print(f'Bet counts: {bet_counts}, balance change: {agent_balance - last_balance}')
                    last_balance = agent_balance
            # reset the game and observe the current state
            deck_state = environment.reset()

            # TODO take the deck state and pass it in to the bet agent to get the bet
            if use_bet_sizes:
                current_bet = bet_agent.select_action(deck_state)
                bet_counts[current_bet] += 1

            # If current_bet is 0 I expect to lose and if current_bet is 1 I expect to win
            current_state = environment.deal_hand()
            bet_reward = 0
            game_end = False
            if current_state == 303:
                bet_reward = 1.5
                if current_bet == 0:
                    bet_reward = -1.5
                # game_end = True
            elif current_state == 202:
                bet_reward = 0
                # game_end = True

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
                    if bet_reward != 1.5:
                        bet_reward = reward
                    if current_bet == 0: # Small size bet - expected to lose
                        bet_reward = -1 * bet_reward # Reward a loss and punish a win

            # opposite_bet = 0
            # if current_bet == 0:
            #     opposite_bet = 1

            if use_bet_sizes:
                bet_agent.learn(deck_state, current_bet, deck_state, bet_reward, True)
            # bet_agent.learn(deck_state, opposite_bet, deck_state, -bet_reward, True)

            if scenario == 1:
                agents_win_rates[a].append(wins / (i + 1.0))
                agents_win_rates_excluding_ties[a].append(wins / max([1, (i + 1.0 - ties)]))
                agents_cumulative_rewards[a].append(cumulative_rewards)
                if use_bet_sizes:
                    agents_balance[a].append(agent_balance)
                    agents_bet_sizes[a].append(BET_SIZE[current_bet])


        if scenario == 1:
            print(f"Agent {a} Win rate: {wins / (num_episodes):.2f}, Win rate excluding ties: {wins / (num_episodes - ties):.2f}")
            print(f"Agent {a} Wins: {wins}, losses: {(num_episodes - ties - wins)}, ties: {ties}")
            if use_bet_sizes:
                print(f'Agent {a} Final balance: {agent_balance}')

        # Exploit only
        if scenario == 2:
            wins = 0
            ties = 0
            agent.epsilon = 0.0
            for i in range(num_episodes):
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
            print(f"Agent {a} win rate while exploiting and excluding ties: {wins / (num_episodes - ties):.2f}")
            print(f"Agent {a} wins: {wins}, losses: {(num_episodes - ties - wins)}, ties: {ties}\n")
            if use_bet_sizes:
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
    if use_bet_sizes:
        np.save('output/agents_bet_sizes', agents_bet_sizes)
        print(f'Bet counts 0: {bet_counts[0]} and 1: {bet_counts[1]}')

    print("Program completed successfully.")

def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs the blackjack simulation')

    parser.add_argument('-t', '--agent-type',
                        choices=['random', 'q-learning','dqn', 'monte-carlo'],
                        default='dqn',
                        help='Type of RL agent (random, q-learning, dqn, or monte-carlo).')

    parser.add_argument('-e', '--num-episodes',
                        type=positive_int,
                        default=100,
                        help='Number of episodes (positive integer).')

    parser.add_argument('-a', '--num-agents',
                        type=positive_int,
                        default=1,
                        help='Number of agents (positive integer).')

    parser.add_argument('-s', '--scenario',
                    type=positive_int,
                    default=1,
                    help='Number of agents (positive integer).')

    parser.add_argument('-b', '--bet-sizes',
                type=bool,
                default=True,
                help='Whether to attempt to learn bet sizes.')

    args = parser.parse_args()
    main(args.scenario, args.agent_type, args.num_episodes, args.num_agents, args.bet_sizes)