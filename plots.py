import matplotlib.pyplot as plt
import numpy as np

def save_cumulative_rewards_plot(agents_cumulative_rewards, output_file, agent_label):
    # agents_cumulative_rewards = np.load(cumulative_rewards_file)
    for i, rewards in enumerate(agents_cumulative_rewards):
        plt.plot(rewards, label=f'Agent {i+1}')

    plt.title(f'{agent_label} Agent Cumulative Rewards Over Time')
    plt.xlabel('Episodes')
    plt.ylabel('Cumulative Rewards')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_agent_balance_plot(agents_balance, output_file, agent_label):
    for i, balance in enumerate(agents_balance):
        plt.plot(balance, label=f'Agent {i+1}')

    plt.title(f'{agent_label} Agent Balance Over Time')
    plt.xlabel('Episodes')
    plt.ylabel('Balance')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_bet_sizes_plot(agents_bet_sizes, output_file, agent_label):
    for i, bet_sizes in enumerate(agents_bet_sizes):
        choices = np.array(bet_sizes)
        cumulative_counts_500 = np.cumsum(choices == 500)
        cumulative_percentage_500 = (cumulative_counts_500 / np.arange(1, len(bet_sizes) + 1)) * 100
        plt.plot(cumulative_percentage_500, label=f'Agent {i+1}')

    plt.title(f'{agent_label} agents cumulative percentage of choosing max bet size over time')
    plt.xlabel('Episode')
    plt.ylabel('Cumulative Percentage')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_win_rates_plot(agents_win_rates, output_file, agent_label):
    for i, win_rates in enumerate(agents_win_rates):
        plt.plot(win_rates, label=f'Agent {i+1}')

    plt.title(f'{agent_label} Agent Win Rates Over Time')
    plt.xlabel('Episodes')
    plt.ylabel('Win rates')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def generate_and_save_plots(timestamp, output_dir, agent_label, agents_win_rates, agents_cumulative_rewards, agents_balance, agents_bet_sizes):
    cr_file = f'{output_dir}/{timestamp}_cumulative_rewards.png'
    save_cumulative_rewards_plot(agents_cumulative_rewards, cr_file, agent_label)

    balance_file = f'{output_dir}/{timestamp}_agent_balance.png'
    save_agent_balance_plot(agents_balance, balance_file, agent_label)

    bet_size_file = f'{output_dir}/{timestamp}_bet_sizes.png'
    save_bet_sizes_plot(agents_bet_sizes, bet_size_file, agent_label)

    win_rates_file = f'{output_dir}/{timestamp}_win_rates.png'
    save_win_rates_plot(agents_win_rates, win_rates_file, agent_label)
