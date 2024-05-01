import matplotlib.pyplot as plt
import numpy as np

def save_cumulative_rewards_plot(agents_cumulative_rewards, output_file, agent_label):
    # agents_cumulative_rewards = np.load(cumulative_rewards_file)
    for i in range(agents_cumulative_rewards.shape[0]):
        plt.plot(agents_cumulative_rewards[i], label=f'Agent {i+1}')

    plt.title(f'{agent_label} Agent Cumulative Rewards Over Time')
    plt.xlabel('Episodes')
    plt.ylabel('Cumulative Rewards')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_agent_balance_plot(agents_balance, output_file, agent_label):
    for i in range(agents_balance.shape[0]):
        plt.plot(agents_balance[i], label=f'Agent {i+1}')

    plt.title(f'{agent_label} Agent Balance Over Time')
    plt.xlabel('Episodes')
    plt.ylabel('Balance')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_bet_sizes_plot_alt(agents_bet_sizes, output_file, agent_label):
    data = agents_bet_sizes[0]
    range_size = 10000
    num_ranges = (len(data) + range_size - 1) // range_size
    count_500 = np.zeros(num_ranges)
    count_10 = np.zeros(num_ranges)

    for i in range(num_ranges):
        start_idx = i * range_size
        end_idx = start_idx + range_size
        count_500[i] = np.sum(np.array(data[start_idx:end_idx]) == 500)
        count_10[i] = np.sum(np.array(data[start_idx:end_idx]) == 10)

    ranges = [f'{i*range_size+1}-{min((i+1)*range_size, len(data))}' for i in range(num_ranges)]
    x = np.arange(len(ranges))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, count_500, width, label='500')
    rects2 = ax.bar(x + width/2, count_10, width, label='10')

    ax.set_xlabel('Episode Ranges')
    ax.set_ylabel('Counts')
    ax.set_title('Counts by choice and episode range')
    ax.set_xticks(x)
    ax.set_xticklabels(ranges)
    ax.legend()

    fig.tight_layout()
    plt.savefig(output_file)
    plt.close()

def save_bet_sizes_plot(agents_bet_sizes, output_file, agent_label):
    for i in range(agents_bet_sizes.shape[0]):
        data = agents_bet_sizes[i]
        choices = np.array(data)
        cumulative_counts_500 = np.cumsum(choices == 500)
        cumulative_percentage_500 = (cumulative_counts_500 / np.arange(1, len(data) + 1)) * 100
        # episodes = np.arange(1, len(data) + 1)
        # plt.figure(figsize=(10, 5))
        # plt.plot(episodes, cumulative_percentage_500, label=f'Agent {i+1}')
        plt.plot(cumulative_percentage_500, label=f'Agent {i+1}')

    plt.title(f'{agent_label} agents cumulative percentage of choosing max bet size over time')
    plt.xlabel('Episode')
    plt.ylabel('Cumulative Percentage')
    # plt.ylim(0, 100)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

def save_win_rates_plot(agents_win_rates, output_file, agent_label):
    for i in range(agents_win_rates.shape[0]):
        plt.plot(agents_win_rates[i], label=f'Agent {i+1}')

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
