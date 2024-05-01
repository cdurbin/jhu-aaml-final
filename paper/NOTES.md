https://cs230.stanford.edu/projects_fall_2021/reports/103066753.pdf - Deep RL with Blackjack and counting cards

460K steps reach min epsilon of 0.01 with self.epsilon_decay=0.99999
230K steps reach epsilon of 0.1

Starting episode 99999001
Agent 0 Win rate: 0.44, Win rate excluding ties: 0.48
Agent 0 Wins: 43951084, losses: 47020622, ties: 9028294
Agent 0 Final balance: -346261750
Mean win rate: 0.44, Mean win rate excluding ties: 0.48
Mean cumulative rewards: -3069538.0
Program completed successfully.
python3 driver.py  55100.75s user 1171.11s system 91% cpu 17:10:03.54 total
Sat Apr  6 18:11:43 EDT 2024


Step 990000: epsilon is now 0.007
Starting episode 995001 Bet counts: {0: 736609, 1: 258391}, balance change: -25365.0
Step 995000: epsilon is now 0.007
Agent 0 Win rate: 0.45, Win rate excluding ties: 0.49
Agent 0 Wins: 449780, losses: 468024, ties: 82196
Agent 0 Final balance: -40485.0
Mean win rate: 0.45, Mean win rate excluding ties: 0.49

## 4 million episodes
Bet counts: {0: 3456819, 1: 542181}, balance change: -1960
Agent 0 Win rate: 0.44, Win rate excluding ties: 0.48
Agent 0 Wins: 1776572, losses: 1928157, ties: 295271
Agent 0 Final balance: -11846030
Mean win rate: 0.44, Mean win rate excluding ties: 0.48
Mean cumulative rewards: -151585.0
Bet counts 0: 3457808 and 1: 542192
Program completed successfully.
python3 driver.py -e 4000000 -t dqn  21690.53s user 1279.95s system 49% cpu 12:51:03.78 total