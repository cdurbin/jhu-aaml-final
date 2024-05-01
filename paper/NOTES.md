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

## BEST SO FAR - lost the settings :(

Starting episode 460001 Bet counts: {0: 441135, 1: 18865}, balance change: -525.0
Step 460001: epsilon is now 0.0001
Starting episode 465001 Bet counts: {0: 446135, 1: 18865}, balance change: -70.0
Step 465001: epsilon is now 0.0001
Starting episode 470001 Bet counts: {0: 451135, 1: 18865}, balance change: 310.0
Step 470001: epsilon is now 0.0001
Starting episode 475001 Bet counts: {0: 456135, 1: 18865}, balance change: 935.0
Step 475001: epsilon is now 0.0001
Starting episode 480001 Bet counts: {0: 461134, 1: 18866}, balance change: 845.0
Step 480001: epsilon is now 0.0001
Starting episode 485001 Bet counts: {0: 466134, 1: 18866}, balance change: -535.0
Step 485001: epsilon is now 0.0001
Starting episode 490001 Bet counts: {0: 471133, 1: 18867}, balance change: 580.0
Step 490001: epsilon is now 0.0001
Starting episode 495001 Bet counts: {0: 476133, 1: 18867}, balance change: 375.0
Step 495001: epsilon is now 0.0001
Starting episode 500001 Bet counts: {0: 481133, 1: 18867}, balance change: 1025.0
Step 500001: epsilon is now 0.0001
Starting episode 505001 Bet counts: {0: 486133, 1: 18867}, balance change: -335.0
Step 505001: epsilon is now 0.0001
Starting episode 510001 Bet counts: {0: 491133, 1: 18867}, balance change: 1070.0
Step 510001: epsilon is now 0.0001
Starting episode 515001 Bet counts: {0: 496132, 1: 18868}, balance change: 1570.0
Step 515001: epsilon is now 0.0001
Starting episode 520001 Bet counts: {0: 501132, 1: 18868}, balance change: 170.0
Step 520001: epsilon is now 0.0001
Starting episode 525001 Bet counts: {0: 506132, 1: 18868}, balance change: 465.0
Step 525001: epsilon is now 0.0001
Starting episode 530001 Bet counts: {0: 511132, 1: 18868}, balance change: 1375.0
Step 530001: epsilon is now 0.0001
Starting episode 535001 Bet counts: {0: 516132, 1: 18868}, balance change: 230.0
Step 535001: epsilon is now 0.0001
Starting episode 540001 Bet counts: {0: 521132, 1: 18868}, balance change: 450.0
Step 540001: epsilon is now 0.0001
Starting episode 545001 Bet counts: {0: 526131, 1: 18869}, balance change: 1710.0
Step 545001: epsilon is now 0.0001
Starting episode 550001 Bet counts: {0: 531131, 1: 18869}, balance change: 250.0
Step 550001: epsilon is now 0.0001
Starting episode 555001 Bet counts: {0: 536130, 1: 18870}, balance change: 1015.0
Step 555001: epsilon is now 0.0001
Starting episode 560001 Bet counts: {0: 541130, 1: 18870}, balance change: 310.0
Step 560001: epsilon is now 0.0001
Starting episode 565001 Bet counts: {0: 546129, 1: 18871}, balance change: 185.0
Step 565001: epsilon is now 0.0001
Starting episode 570001 Bet counts: {0: 551128, 1: 18872}, balance change: -75.0
Step 570001: epsilon is now 0.0001
Starting episode 575001 Bet counts: {0: 556128, 1: 18872}, balance change: -1530.0
Step 575001: epsilon is now 0.0001
Starting episode 580001 Bet counts: {0: 561128, 1: 18872}, balance change: 710.0
Step 580001: epsilon is now 0.0001
Starting episode 585001 Bet counts: {0: 566127, 1: 18873}, balance change: -765.0
Step 585001: epsilon is now 0.0001
Starting episode 590001 Bet counts: {0: 571127, 1: 18873}, balance change: 1665.0
Step 590001: epsilon is now 0.0001
Starting episode 595001 Bet counts: {0: 576127, 1: 18873}, balance change: -120.0
Step 595001: epsilon is now 0.0001
Starting episode 600001 Bet counts: {0: 581127, 1: 18873}, balance change: 1055.0
Step 600001: epsilon is now 0.0001
Starting episode 605001 Bet counts: {0: 586127, 1: 18873}, balance change: -920.0
Step 605001: epsilon is now 0.0001
Starting episode 610001 Bet counts: {0: 591126, 1: 18874}, balance change: 1160.0
Step 610001: epsilon is now 0.0001
Starting episode 615001 Bet counts: {0: 596125, 1: 18875}, balance change: -395.0
Step 615001: epsilon is now 0.0001
Starting episode 620001 Bet counts: {0: 601125, 1: 18875}, balance change: -585.0
Step 620001: epsilon is now 0.0001
Starting episode 625001 Bet counts: {0: 606125, 1: 18875}, balance change: 160.0
Step 625001: epsilon is now 0.0001
Starting episode 630001 Bet counts: {0: 611125, 1: 18875}, balance change: 800.0
Step 630001: epsilon is now 0.0001
Starting episode 635001 Bet counts: {0: 616125, 1: 18875}, balance change: 1080.0
Step 635001: epsilon is now 0.0001
Starting episode 640001 Bet counts: {0: 621125, 1: 18875}, balance change: 60.0
Step 640001: epsilon is now 0.0001
Starting episode 645001 Bet counts: {0: 626125, 1: 18875}, balance change: -1160.0
Step 645001: epsilon is now 0.0001
Starting episode 650001 Bet counts: {0: 631124, 1: 18876}, balance change: -1430.0
Step 650001: epsilon is now 0.0001
Starting episode 655001 Bet counts: {0: 636124, 1: 18876}, balance change: 15.0
Step 655001: epsilon is now 0.0001
Starting episode 660001 Bet counts: {0: 641123, 1: 18877}, balance change: -505.0
Step 660001: epsilon is now 0.0001
Starting episode 665001 Bet counts: {0: 646122, 1: 18878}, balance change: 250.0
Step 665001: epsilon is now 0.0001
Starting episode 670001 Bet counts: {0: 651122, 1: 18878}, balance change: 925.0
Step 670001: epsilon is now 0.0001
Starting episode 675001 Bet counts: {0: 656122, 1: 18878}, balance change: -685.0
Step 675001: epsilon is now 0.0001
Starting episode 680001 Bet counts: {0: 661122, 1: 18878}, balance change: 390.0
Step 680001: epsilon is now 0.0001
Starting episode 685001 Bet counts: {0: 666122, 1: 18878}, balance change: 720.0
Step 685001: epsilon is now 0.0001
Starting episode 690001 Bet counts: {0: 671122, 1: 18878}, balance change: -115.0
Step 690001: epsilon is now 0.0001
Starting episode 695001 Bet counts: {0: 676122, 1: 18878}, balance change: -335.0
Step 695001: epsilon is now 0.0001
Starting episode 700001 Bet counts: {0: 681121, 1: 18879}, balance change: -195.0
Step 700001: epsilon is now 0.0001
Starting episode 705001 Bet counts: {0: 686120, 1: 18880}, balance change: 785.0
Step 705001: epsilon is now 0.0001
Starting episode 710001 Bet counts: {0: 691120, 1: 18880}, balance change: 70.0
Step 710001: epsilon is now 0.0001
Starting episode 715001 Bet counts: {0: 696120, 1: 18880}, balance change: 900.0
Step 715001: epsilon is now 0.0001
Starting episode 720001 Bet counts: {0: 701120, 1: 18880}, balance change: 300.0
Step 720001: epsilon is now 0.0001
Starting episode 725001 Bet counts: {0: 706120, 1: 18880}, balance change: 55.0
Step 725001: epsilon is now 0.0001
Starting episode 730001 Bet counts: {0: 711120, 1: 18880}, balance change: 55.0
Step 730001: epsilon is now 0.0001
Starting episode 735001 Bet counts: {0: 716120, 1: 18880}, balance change: 715.0
Step 735001: epsilon is now 0.0001
Starting episode 740001 Bet counts: {0: 721120, 1: 18880}, balance change: -205.0
Step 740001: epsilon is now 0.0001
Starting episode 745001 Bet counts: {0: 726120, 1: 18880}, balance change: 640.0
Step 745001: epsilon is now 0.0001
Starting episode 750001 Bet counts: {0: 731120, 1: 18880}, balance change: -980.0
Step 750001: epsilon is now 0.0001
Starting episode 755001 Bet counts: {0: 736120, 1: 18880}, balance change: -1265.0
Step 755001: epsilon is now 0.0001
Starting episode 760001 Bet counts: {0: 741120, 1: 18880}, balance change: -475.0
Step 760001: epsilon is now 0.0001
Starting episode 765001 Bet counts: {0: 746120, 1: 18880}, balance change: 1890.0
Step 765001: epsilon is now 0.0001
Starting episode 770001 Bet counts: {0: 751120, 1: 18880}, balance change: 1105.0
Step 770001: epsilon is now 0.0001
Starting episode 775001 Bet counts: {0: 756120, 1: 18880}, balance change: 1270.0
Step 775001: epsilon is now 0.0001
Starting episode 780001 Bet counts: {0: 761119, 1: 18881}, balance change: -25.0
Step 780001: epsilon is now 0.0001
Starting episode 785001 Bet counts: {0: 766119, 1: 18881}, balance change: -1135.0
Step 785001: epsilon is now 0.0001
Starting episode 790001 Bet counts: {0: 771119, 1: 18881}, balance change: 140.0
Step 790001: epsilon is now 0.0001
Starting episode 795001 Bet counts: {0: 776119, 1: 18881}, balance change: 920.0
Step 795001: epsilon is now 0.0001
Starting episode 800001 Bet counts: {0: 781119, 1: 18881}, balance change: 1000.0
Step 800001: epsilon is now 0.0001
Starting episode 805001 Bet counts: {0: 786119, 1: 18881}, balance change: -730.0
Step 805001: epsilon is now 0.0001
Starting episode 810001 Bet counts: {0: 791119, 1: 18881}, balance change: -60.0
Step 810001: epsilon is now 0.0001
Starting episode 815001 Bet counts: {0: 796118, 1: 18882}, balance change: 930.0
Step 815001: epsilon is now 0.0001
Starting episode 820001 Bet counts: {0: 801118, 1: 18882}, balance change: 590.0
Step 820001: epsilon is now 0.0001
Starting episode 825001 Bet counts: {0: 806117, 1: 18883}, balance change: -215.0
Step 825001: epsilon is now 0.0001
Starting episode 830001 Bet counts: {0: 811116, 1: 18884}, balance change: -1370.0
Step 830001: epsilon is now 0.0001
Starting episode 835001 Bet counts: {0: 816115, 1: 18885}, balance change: 1110.0
Step 835001: epsilon is now 0.0001
Starting episode 840001 Bet counts: {0: 821115, 1: 18885}, balance change: 845.0
Step 840001: epsilon is now 0.0001
Starting episode 845001 Bet counts: {0: 826114, 1: 18886}, balance change: 2425.0
Step 845001: epsilon is now 0.0001
Starting episode 850001 Bet counts: {0: 831091, 1: 18909}, balance change: -1045.0
Step 850001: epsilon is now 0.0001
Starting episode 855001 Bet counts: {0: 836059, 1: 18941}, balance change: 1335.0
Step 855001: epsilon is now 0.0001
Starting episode 860001 Bet counts: {0: 841028, 1: 18972}, balance change: -4880.0
Step 860001: epsilon is now 0.0001
Starting episode 865001 Bet counts: {0: 846025, 1: 18975}, balance change: 1285.0
Step 865001: epsilon is now 0.0001
Starting episode 870001 Bet counts: {0: 851024, 1: 18976}, balance change: 345.0
Step 870001: epsilon is now 0.0001
Starting episode 875001 Bet counts: {0: 856022, 1: 18978}, balance change: 830.0
Step 875001: epsilon is now 0.0001
Starting episode 880001 Bet counts: {0: 861017, 1: 18983}, balance change: -505.0
Step 880001: epsilon is now 0.0001
Starting episode 885001 Bet counts: {0: 866012, 1: 18988}, balance change: 1375.0
Step 885001: epsilon is now 0.0001
Starting episode 890001 Bet counts: {0: 871009, 1: 18991}, balance change: 755.0
Step 890001: epsilon is now 0.0001
Starting episode 895001 Bet counts: {0: 875998, 1: 19002}, balance change: -2785.0
Step 895001: epsilon is now 0.0001
Starting episode 900001 Bet counts: {0: 880985, 1: 19015}, balance change: -715.0
Step 900001: epsilon is now 0.0001
Starting episode 905001 Bet counts: {0: 885981, 1: 19019}, balance change: 505.0
Step 905001: epsilon is now 0.0001
Starting episode 910001 Bet counts: {0: 890972, 1: 19028}, balance change: -125.0
Step 910001: epsilon is now 0.0001
Starting episode 915001 Bet counts: {0: 895966, 1: 19034}, balance change: -805.0
Step 915001: epsilon is now 0.0001
Starting episode 920001 Bet counts: {0: 900961, 1: 19039}, balance change: -995.0
Step 920001: epsilon is now 0.0001
Starting episode 925001 Bet counts: {0: 905955, 1: 19045}, balance change: 1555.0
Step 925001: epsilon is now 0.0001
Starting episode 930001 Bet counts: {0: 910938, 1: 19062}, balance change: 1315.0
Step 930001: epsilon is now 0.0001
Starting episode 935001 Bet counts: {0: 915925, 1: 19075}, balance change: 2155.0
Step 935001: epsilon is now 0.0001
Starting episode 940001 Bet counts: {0: 920905, 1: 19095}, balance change: 2160.0
Step 940001: epsilon is now 0.0001
Starting episode 945001 Bet counts: {0: 925890, 1: 19110}, balance change: -2525.0
Step 945001: epsilon is now 0.0001
Starting episode 950001 Bet counts: {0: 930867, 1: 19133}, balance change: 1550.0
Step 950001: epsilon is now 0.0001
Starting episode 955001 Bet counts: {0: 935849, 1: 19151}, balance change: -1170.0
Step 955001: epsilon is now 0.0001
Starting episode 960001 Bet counts: {0: 940837, 1: 19163}, balance change: 3300.0
Step 960001: epsilon is now 0.0001
Starting episode 965001 Bet counts: {0: 945822, 1: 19178}, balance change: 420.0
Step 965001: epsilon is now 0.0001
Starting episode 970001 Bet counts: {0: 950814, 1: 19186}, balance change: -1335.0
Step 970001: epsilon is now 0.0001
Starting episode 975001 Bet counts: {0: 955814, 1: 19186}, balance change: -500.0
Step 975001: epsilon is now 0.0001
Starting episode 980001 Bet counts: {0: 960812, 1: 19188}, balance change: -35.0
Step 980001: epsilon is now 0.0001
Starting episode 985001 Bet counts: {0: 965810, 1: 19190}, balance change: 2130.0
Step 985001: epsilon is now 0.0001
Starting episode 990001 Bet counts: {0: 970809, 1: 19191}, balance change: -220.0
Step 990001: epsilon is now 0.0001
Starting episode 995001 Bet counts: {0: 975808, 1: 19192}, balance change: -375.0
Step 995001: epsilon is now 0.0001
Agent 1 Win rate: 0.44, Win rate excluding ties: 0.49
Agent 1 Wins: 444182, losses: 465761, ties: 90057
Agent 1 Final balance: -55060.0
Mean win rate: 0.44, Mean win rate excluding ties: 0.49
Mean cumulative rewards: -22040.5
Bet counts 0: 980807 and 1: 19193
Program completed successfully.
python3 driver.py -e 1000000 -t q-learning -b dqn -a 2  7684.14s user 423.87s system 110% cpu 2:02:46.49 total
(aaml-final) ➜  code git:(main) ✗ time python driver.py -e 1000000 -t q-learning -b dqn -a 2
Running with 2 q-learning agents and 1000000 episodes
Device is cpu
Starting episode 1 Bet counts: {0: 0, 1: 0}, balance change: 0
Starting episode 5001 Bet counts: {0: 2535, 1: 2465}, balance change: -61670.0
Step 5001: epsilon is now 0.9753
Starting episode 10001 Bet counts: {0: 5007, 1: 4993}, balance change: 25170.0
Step 10001: epsilon is now 0.9512
Starting episode 15001 Bet counts: {0: 7476, 1: 7524}, balance change: 5905.0
Step 15001: epsilon is now 0.9277
Starting episode 20001 Bet counts: {0: 10001, 1: 9999}, balance change: 1740.0
Step 20001: epsilon is now 0.9048
Starting episode 25001 Bet counts: {0: 12509, 1: 12491}, balance change: -22400.0
Step 25001: epsilon is now 0.8825
Starting episode 30001 Bet counts: {0: 15103, 1: 14897}, balance change: -12870.0
Step 30001: epsilon is now 0.8607
Starting episode 35001 Bet counts: {0: 17707, 1: 17293}, balance change: -28415.0
Step 35001: epsilon is now 0.8395
Starting episode 40001 Bet counts: {0: 20354, 1: 19646}, balance change: 540.0
Step 40001: epsilon is now 0.8187
Starting episode 45001 Bet counts: {0: 23079, 1: 21921}, balance change: -18615.0
Step 45001: epsilon is now 0.7985
Starting episode 50001 Bet counts: {0: 25907, 1: 24093}, balance change: -9275.0
Step 50001: epsilon is now 0.7788
Starting episode 55001 Bet counts: {0: 28803, 1: 26197}, balance change: 12595.0
Step 55001: epsilon is now 0.7596
Starting episode 60001 Bet counts: {0: 31553, 1: 28447}, balance change: -5990.0
Step 60001: epsilon is now 0.7408
Starting episode 65001 Bet counts: {0: 34329, 1: 30671}, balance change: 16660.0
Step 65001: epsilon is now 0.7225
Starting episode 70001 Bet counts: {0: 36947, 1: 33053}, balance change: -805.0
Step 70001: epsilon is now 0.7047
Starting episode 75001 Bet counts: {0: 39699, 1: 35301}, balance change: -3225.0
Step 75001: epsilon is now 0.6873
Starting episode 80001 Bet counts: {0: 42344, 1: 37656}, balance change: -14565.0
Step 80001: epsilon is now 0.6703
Starting episode 85001 Bet counts: {0: 45132, 1: 39868}, balance change: 14065.0
Step 85001: epsilon is now 0.6538
Starting episode 90001 Bet counts: {0: 47884, 1: 42116}, balance change: 33745.0
Step 90001: epsilon is now 0.6376
Starting episode 95001 Bet counts: {0: 50597, 1: 44403}, balance change: -29610.0
Step 95001: epsilon is now 0.6219
Starting episode 100001 Bet counts: {0: 53236, 1: 46764}, balance change: -6780.0
Step 100001: epsilon is now 0.6065
Starting episode 105001 Bet counts: {0: 55807, 1: 49193}, balance change: -39750.0
Step 105001: epsilon is now 0.5916
Starting episode 110001 Bet counts: {0: 58607, 1: 51393}, balance change: 25815.0
Step 110001: epsilon is now 0.5769
Starting episode 115001 Bet counts: {0: 61591, 1: 53409}, balance change: 25785.0
Step 115001: epsilon is now 0.5627
Starting episode 120001 Bet counts: {0: 64553, 1: 55447}, balance change: 28255.0
Step 120001: epsilon is now 0.5488
Starting episode 125001 Bet counts: {0: 67219, 1: 57781}, balance change: 20010.0
Step 125001: epsilon is now 0.5353
Starting episode 130001 Bet counts: {0: 70226, 1: 59774}, balance change: 46890.0
Step 130001: epsilon is now 0.5220
Starting episode 135001 Bet counts: {0: 73210, 1: 61790}, balance change: -6385.0
Step 135001: epsilon is now 0.5092
Starting episode 140001 Bet counts: {0: 76069, 1: 63931}, balance change: 2305.0
Step 140001: epsilon is now 0.4966
Starting episode 145001 Bet counts: {0: 79220, 1: 65780}, balance change: 20705.0
Step 145001: epsilon is now 0.4843
Starting episode 150001 Bet counts: {0: 81931, 1: 68069}, balance change: 41905.0
Step 150001: epsilon is now 0.4724
Starting episode 155001 Bet counts: {0: 84430, 1: 70570}, balance change: -48410.0
Step 155001: epsilon is now 0.4607
Starting episode 160001 Bet counts: {0: 87261, 1: 72739}, balance change: 11145.0
Step 160001: epsilon is now 0.4493
Starting episode 165001 Bet counts: {0: 90185, 1: 74815}, balance change: 14730.0
Step 165001: epsilon is now 0.4382
Starting episode 170001 Bet counts: {0: 93130, 1: 76870}, balance change: -21975.0
Step 170001: epsilon is now 0.4274
Starting episode 175001 Bet counts: {0: 95870, 1: 79130}, balance change: 2035.0
Step 175001: epsilon is now 0.4169
Starting episode 180001 Bet counts: {0: 98735, 1: 81265}, balance change: 41630.0
Step 180001: epsilon is now 0.4066
Starting episode 185001 Bet counts: {0: 101660, 1: 83340}, balance change: 4585.0
Step 185001: epsilon is now 0.3965
Starting episode 190001 Bet counts: {0: 104605, 1: 85395}, balance change: -30690.0
Step 190001: epsilon is now 0.3867
Starting episode 195001 Bet counts: {0: 107519, 1: 87481}, balance change: 15790.0
Step 195001: epsilon is now 0.3772
Starting episode 200001 Bet counts: {0: 110451, 1: 89549}, balance change: -9190.0
Step 200001: epsilon is now 0.3679
Starting episode 205001 Bet counts: {0: 113120, 1: 91880}, balance change: -18790.0
Step 205001: epsilon is now 0.3588
Starting episode 210001 Bet counts: {0: 116459, 1: 93541}, balance change: -37690.0
Step 210001: epsilon is now 0.3499
Starting episode 215001 Bet counts: {0: 119532, 1: 95468}, balance change: 35745.0
Step 215001: epsilon is now 0.3413
Starting episode 220001 Bet counts: {0: 122641, 1: 97359}, balance change: -25155.0
Step 220001: epsilon is now 0.3329
Starting episode 225001 Bet counts: {0: 126102, 1: 98898}, balance change: -16600.0
Step 225001: epsilon is now 0.3247
Starting episode 230001 Bet counts: {0: 129371, 1: 100629}, balance change: -17595.0
Step 230001: epsilon is now 0.3166
Starting episode 235001 Bet counts: {0: 132245, 1: 102755}, balance change: 14540.0
Step 235001: epsilon is now 0.3088
Starting episode 240001 Bet counts: {0: 135518, 1: 104482}, balance change: 8635.0
Step 240001: epsilon is now 0.3012
Starting episode 245001 Bet counts: {0: 139074, 1: 105926}, balance change: -15995.0
Step 245001: epsilon is now 0.2938
Starting episode 250001 Bet counts: {0: 142492, 1: 107508}, balance change: 15690.0
Step 250001: epsilon is now 0.2865
Starting episode 255001 Bet counts: {0: 146300, 1: 108700}, balance change: -335.0
Step 255001: epsilon is now 0.2794
Starting episode 260001 Bet counts: {0: 149684, 1: 110316}, balance change: 39155.0
Step 260001: epsilon is now 0.2725
Starting episode 265001 Bet counts: {0: 153278, 1: 111722}, balance change: 7695.0
Step 265001: epsilon is now 0.2658
Starting episode 270001 Bet counts: {0: 156984, 1: 113016}, balance change: 1895.0
Step 270001: epsilon is now 0.2592
Starting episode 275001 Bet counts: {0: 160189, 1: 114811}, balance change: -19200.0
Step 275001: epsilon is now 0.2528
Starting episode 280001 Bet counts: {0: 163975, 1: 116025}, balance change: -5630.0
Step 280001: epsilon is now 0.2466
Starting episode 285001 Bet counts: {0: 167502, 1: 117498}, balance change: -23445.0
Step 285001: epsilon is now 0.2405
Starting episode 290001 Bet counts: {0: 170616, 1: 119384}, balance change: -8535.0
Step 290001: epsilon is now 0.2346
Starting episode 295001 Bet counts: {0: 174142, 1: 120858}, balance change: 8925.0
Step 295001: epsilon is now 0.2288
Starting episode 300001 Bet counts: {0: 177600, 1: 122400}, balance change: -13365.0
Step 300001: epsilon is now 0.2231
Starting episode 305001 Bet counts: {0: 181148, 1: 123852}, balance change: -4135.0
Step 305001: epsilon is now 0.2176
Starting episode 310001 Bet counts: {0: 184718, 1: 125282}, balance change: -20860.0
Step 310001: epsilon is now 0.2122
Starting episode 315001 Bet counts: {0: 188698, 1: 126302}, balance change: -2975.0
Step 315001: epsilon is now 0.2070
Starting episode 320001 Bet counts: {0: 192555, 1: 127445}, balance change: 1210.0
Step 320001: epsilon is now 0.2019
Starting episode 325001 Bet counts: {0: 196038, 1: 128962}, balance change: 14225.0
Step 325001: epsilon is now 0.1969
Starting episode 330001 Bet counts: {0: 200012, 1: 129988}, balance change: 7005.0
Step 330001: epsilon is now 0.1920
Starting episode 335001 Bet counts: {0: 203823, 1: 131177}, balance change: 1310.0
Step 335001: epsilon is now 0.1873
Starting episode 340001 Bet counts: {0: 207854, 1: 132146}, balance change: 9185.0
Step 340001: epsilon is now 0.1827
Starting episode 345001 Bet counts: {0: 211902, 1: 133098}, balance change: 16350.0
Step 345001: epsilon is now 0.1782
Starting episode 350001 Bet counts: {0: 215881, 1: 134119}, balance change: 5570.0
Step 350001: epsilon is now 0.1738
Starting episode 355001 Bet counts: {0: 220086, 1: 134914}, balance change: -9700.0
Step 355001: epsilon is now 0.1695
Starting episode 360001 Bet counts: {0: 224343, 1: 135657}, balance change: -11850.0
Step 360001: epsilon is now 0.1653
Starting episode 365001 Bet counts: {0: 227985, 1: 137015}, balance change: -6005.0
Step 365001: epsilon is now 0.1612
Starting episode 370001 Bet counts: {0: 231784, 1: 138216}, balance change: -18435.0
Step 370001: epsilon is now 0.1572
Starting episode 375001 Bet counts: {0: 235725, 1: 139275}, balance change: -2980.0
Step 375001: epsilon is now 0.1534
Starting episode 380001 Bet counts: {0: 239740, 1: 140260}, balance change: -5695.0
Step 380001: epsilon is now 0.1496
Starting episode 385001 Bet counts: {0: 244000, 1: 141000}, balance change: -710.0
Step 385001: epsilon is now 0.1459
Starting episode 390001 Bet counts: {0: 248239, 1: 141761}, balance change: 27020.0
Step 390001: epsilon is now 0.1423
Starting episode 395001 Bet counts: {0: 252416, 1: 142584}, balance change: 18605.0
Step 395001: epsilon is now 0.1388
Starting episode 400001 Bet counts: {0: 256614, 1: 143386}, balance change: -3475.0
Step 400001: epsilon is now 0.1353
Starting episode 405001 Bet counts: {0: 260498, 1: 144502}, balance change: -11645.0
Step 405001: epsilon is now 0.1320
Starting episode 410001 Bet counts: {0: 264257, 1: 145743}, balance change: -8430.0
Step 410001: epsilon is now 0.1287
Starting episode 415001 Bet counts: {0: 268335, 1: 146665}, balance change: -12290.0
Step 415001: epsilon is now 0.1256
Starting episode 420001 Bet counts: {0: 272170, 1: 147830}, balance change: 48735.0
Step 420001: epsilon is now 0.1225
Starting episode 425001 Bet counts: {0: 275710, 1: 149290}, balance change: -29115.0
Step 425001: epsilon is now 0.1194
Starting episode 430001 Bet counts: {0: 279330, 1: 150670}, balance change: 7040.0
Step 430001: epsilon is now 0.1165
Starting episode 435001 Bet counts: {0: 282898, 1: 152102}, balance change: 11995.0
Step 435001: epsilon is now 0.1136
Starting episode 440001 Bet counts: {0: 286725, 1: 153275}, balance change: -20815.0
Step 440001: epsilon is now 0.1108
Starting episode 445001 Bet counts: {0: 290150, 1: 154850}, balance change: -6200.0
Step 445001: epsilon is now 0.1081
Starting episode 450001 Bet counts: {0: 294376, 1: 155624}, balance change: 9820.0
Step 450001: epsilon is now 0.1054
Starting episode 455001 Bet counts: {0: 298359, 1: 156641}, balance change: -3790.0
Step 455001: epsilon is now 0.1028
Starting episode 460001 Bet counts: {0: 301977, 1: 158023}, balance change: -25510.0
Step 460001: epsilon is now 0.1003
Starting episode 465001 Bet counts: {0: 306119, 1: 158881}, balance change: -3070.0
Step 465001: epsilon is now 0.0978
Starting episode 470001 Bet counts: {0: 310313, 1: 159687}, balance change: -15155.0
Step 470001: epsilon is now 0.0954
Starting episode 475001 Bet counts: {0: 314240, 1: 160760}, balance change: 13020.0
Step 475001: epsilon is now 0.0930
Starting episode 480001 Bet counts: {0: 318395, 1: 161605}, balance change: 1215.0
Step 480001: epsilon is now 0.0907
Starting episode 485001 Bet counts: {0: 322458, 1: 162542}, balance change: 16335.0
Step 485001: epsilon is now 0.0885
Starting episode 490001 Bet counts: {0: 326199, 1: 163801}, balance change: 14305.0
Step 490001: epsilon is now 0.0863
Starting episode 495001 Bet counts: {0: 329974, 1: 165026}, balance change: -19205.0
Step 495001: epsilon is now 0.0842
Starting episode 500001 Bet counts: {0: 333706, 1: 166294}, balance change: 19195.0
Step 500001: epsilon is now 0.0821
Starting episode 505001 Bet counts: {0: 337610, 1: 167390}, balance change: -14435.0
Step 505001: epsilon is now 0.0801
Starting episode 510001 Bet counts: {0: 341594, 1: 168406}, balance change: 12085.0
Step 510001: epsilon is now 0.0781
Starting episode 515001 Bet counts: {0: 345096, 1: 169904}, balance change: 7960.0
Step 515001: epsilon is now 0.0762
Starting episode 520001 Bet counts: {0: 348791, 1: 171209}, balance change: 2490.0
Step 520001: epsilon is now 0.0743
Starting episode 525001 Bet counts: {0: 352858, 1: 172142}, balance change: 1375.0
Step 525001: epsilon is now 0.0724
Starting episode 530001 Bet counts: {0: 357073, 1: 172927}, balance change: -3325.0
Step 530001: epsilon is now 0.0707
Starting episode 535001 Bet counts: {0: 361552, 1: 173448}, balance change: 5250.0
Step 535001: epsilon is now 0.0689
Starting episode 540001 Bet counts: {0: 364822, 1: 175178}, balance change: -3245.0
Step 540001: epsilon is now 0.0672
Starting episode 545001 Bet counts: {0: 368434, 1: 176566}, balance change: 20050.0
Step 545001: epsilon is now 0.0655
Starting episode 550001 Bet counts: {0: 371056, 1: 178944}, balance change: -32320.0
Step 550001: epsilon is now 0.0639
Starting episode 555001 Bet counts: {0: 373510, 1: 181490}, balance change: 46725.0
Step 555001: epsilon is now 0.0623
Starting episode 560001 Bet counts: {0: 376922, 1: 183078}, balance change: 2555.0
Step 560001: epsilon is now 0.0608
Starting episode 565001 Bet counts: {0: 380830, 1: 184170}, balance change: 26470.0
Step 565001: epsilon is now 0.0593
Starting episode 570001 Bet counts: {0: 383287, 1: 186713}, balance change: 19225.0
Step 570001: epsilon is now 0.0578
Starting episode 575001 Bet counts: {0: 386204, 1: 188796}, balance change: 1685.0
Step 575001: epsilon is now 0.0564
Starting episode 580001 Bet counts: {0: 389069, 1: 190931}, balance change: 35175.0
Step 580001: epsilon is now 0.0550
Starting episode 585001 Bet counts: {0: 391897, 1: 193103}, balance change: -16520.0
Step 585001: epsilon is now 0.0537
Starting episode 590001 Bet counts: {0: 395152, 1: 194848}, balance change: -26030.0
Step 590001: epsilon is now 0.0523
Starting episode 595001 Bet counts: {0: 398494, 1: 196506}, balance change: 39400.0
Step 595001: epsilon is now 0.0510
Starting episode 600001 Bet counts: {0: 401252, 1: 198748}, balance change: -39665.0
Step 600001: epsilon is now 0.0498
Starting episode 605001 Bet counts: {0: 404484, 1: 200516}, balance change: -10695.0
Step 605001: epsilon is now 0.0486
Starting episode 610001 Bet counts: {0: 407794, 1: 202206}, balance change: 5455.0
Step 610001: epsilon is now 0.0474
Starting episode 615001 Bet counts: {0: 410463, 1: 204537}, balance change: 14715.0
Step 615001: epsilon is now 0.0462
Starting episode 620001 Bet counts: {0: 414040, 1: 205960}, balance change: 19950.0
Step 620001: epsilon is now 0.0450
Starting episode 625001 Bet counts: {0: 417652, 1: 207348}, balance change: 4995.0
Step 625001: epsilon is now 0.0439
Starting episode 630001 Bet counts: {0: 421456, 1: 208544}, balance change: 2750.0
Step 630001: epsilon is now 0.0429
Starting episode 635001 Bet counts: {0: 424486, 1: 210514}, balance change: -4475.0
Step 635001: epsilon is now 0.0418
Starting episode 640001 Bet counts: {0: 428487, 1: 211513}, balance change: -11175.0
Step 640001: epsilon is now 0.0408
Starting episode 645001 Bet counts: {0: 432452, 1: 212548}, balance change: 420.0
Step 645001: epsilon is now 0.0398
Starting episode 650001 Bet counts: {0: 436192, 1: 213808}, balance change: -26975.0
Step 650001: epsilon is now 0.0388
Starting episode 655001 Bet counts: {0: 439711, 1: 215289}, balance change: 27620.0
Step 655001: epsilon is now 0.0378
Starting episode 660001 Bet counts: {0: 443997, 1: 216003}, balance change: -17060.0
Step 660001: epsilon is now 0.0369
Starting episode 665001 Bet counts: {0: 448388, 1: 216612}, balance change: 4890.0
Step 665001: epsilon is now 0.0360
Starting episode 670001 Bet counts: {0: 452669, 1: 217331}, balance change: 10000.0
Step 670001: epsilon is now 0.0351
Starting episode 675001 Bet counts: {0: 456891, 1: 218109}, balance change: 3825.0
Step 675001: epsilon is now 0.0342
Starting episode 680001 Bet counts: {0: 460637, 1: 219363}, balance change: -13360.0
Step 680001: epsilon is now 0.0334
Starting episode 685001 Bet counts: {0: 464971, 1: 220029}, balance change: 9790.0
Step 685001: epsilon is now 0.0325
Starting episode 690001 Bet counts: {0: 469737, 1: 220263}, balance change: 11375.0
Step 690001: epsilon is now 0.0317
Starting episode 695001 Bet counts: {0: 474498, 1: 220502}, balance change: -1220.0
Step 695001: epsilon is now 0.0310
Starting episode 700001 Bet counts: {0: 479216, 1: 220784}, balance change: 18095.0
Step 700001: epsilon is now 0.0302
Starting episode 705001 Bet counts: {0: 483868, 1: 221132}, balance change: 3305.0
Step 705001: epsilon is now 0.0295
Starting episode 710001 Bet counts: {0: 488620, 1: 221380}, balance change: 1835.0
Step 710001: epsilon is now 0.0287
Starting episode 715001 Bet counts: {0: 493392, 1: 221608}, balance change: 7550.0
Step 715001: epsilon is now 0.0280
Starting episode 720001 Bet counts: {0: 498170, 1: 221830}, balance change: -8030.0
Step 720001: epsilon is now 0.0273
Starting episode 725001 Bet counts: {0: 502900, 1: 222100}, balance change: -12485.0
Step 725001: epsilon is now 0.0266
Starting episode 730001 Bet counts: {0: 507625, 1: 222375}, balance change: -965.0
Step 730001: epsilon is now 0.0260
Starting episode 735001 Bet counts: {0: 512347, 1: 222653}, balance change: 11940.0
Step 735001: epsilon is now 0.0253
Starting episode 740001 Bet counts: {0: 516914, 1: 223086}, balance change: -7545.0
Step 740001: epsilon is now 0.0247
Starting episode 745001 Bet counts: {0: 521443, 1: 223557}, balance change: 6525.0
Step 745001: epsilon is now 0.0241
Starting episode 750001 Bet counts: {0: 525457, 1: 224543}, balance change: 2620.0
Step 750001: epsilon is now 0.0235
Starting episode 755001 Bet counts: {0: 529876, 1: 225124}, balance change: 7875.0
Step 755001: epsilon is now 0.0229
Starting episode 760001 Bet counts: {0: 533736, 1: 226264}, balance change: -6090.0
Step 760001: epsilon is now 0.0224
Starting episode 765001 Bet counts: {0: 537830, 1: 227170}, balance change: 19555.0
Step 765001: epsilon is now 0.0218
Starting episode 770001 Bet counts: {0: 541708, 1: 228292}, balance change: 10685.0
Step 770001: epsilon is now 0.0213
Starting episode 775001 Bet counts: {0: 545247, 1: 229753}, balance change: 1995.0
Step 775001: epsilon is now 0.0208
Starting episode 780001 Bet counts: {0: 548995, 1: 231005}, balance change: -12785.0
Step 780001: epsilon is now 0.0202
Starting episode 785001 Bet counts: {0: 552840, 1: 232160}, balance change: 10300.0
Step 785001: epsilon is now 0.0197
Starting episode 790001 Bet counts: {0: 556899, 1: 233101}, balance change: -1175.0
Step 790001: epsilon is now 0.0193
Starting episode 795001 Bet counts: {0: 561230, 1: 233770}, balance change: 5190.0
Step 795001: epsilon is now 0.0188
Starting episode 800001 Bet counts: {0: 565676, 1: 234324}, balance change: -3040.0
Step 800001: epsilon is now 0.0183
Starting episode 805001 Bet counts: {0: 570250, 1: 234750}, balance change: 915.0
Step 805001: epsilon is now 0.0179
Starting episode 810001 Bet counts: {0: 574876, 1: 235124}, balance change: 4535.0
Step 810001: epsilon is now 0.0174
Starting episode 815001 Bet counts: {0: 579340, 1: 235660}, balance change: 1820.0
Step 815001: epsilon is now 0.0170
Starting episode 820001 Bet counts: {0: 583832, 1: 236168}, balance change: 5155.0
Step 820001: epsilon is now 0.0166
Starting episode 825001 Bet counts: {0: 588369, 1: 236631}, balance change: 9365.0
Step 825001: epsilon is now 0.0162
Starting episode 830001 Bet counts: {0: 593038, 1: 236962}, balance change: -11605.0
Step 830001: epsilon is now 0.0158
Starting episode 835001 Bet counts: {0: 597795, 1: 237205}, balance change: 7390.0
Step 835001: epsilon is now 0.0154
Starting episode 840001 Bet counts: {0: 602560, 1: 237440}, balance change: 2820.0
Step 840001: epsilon is now 0.0150
Starting episode 845001 Bet counts: {0: 607304, 1: 237696}, balance change: -195.0
Step 845001: epsilon is now 0.0146
Starting episode 850001 Bet counts: {0: 612095, 1: 237905}, balance change: 4080.0
Step 850001: epsilon is now 0.0143
Starting episode 855001 Bet counts: {0: 616900, 1: 238100}, balance change: 9520.0
Step 855001: epsilon is now 0.0139
Starting episode 860001 Bet counts: {0: 621684, 1: 238316}, balance change: 8110.0
Step 860001: epsilon is now 0.0136
Starting episode 865001 Bet counts: {0: 626514, 1: 238486}, balance change: -8815.0
Step 865001: epsilon is now 0.0132
Starting episode 870001 Bet counts: {0: 631275, 1: 238725}, balance change: -2420.0
Step 870001: epsilon is now 0.0129
Starting episode 875001 Bet counts: {0: 636065, 1: 238935}, balance change: 7875.0
Step 875001: epsilon is now 0.0126
Starting episode 880001 Bet counts: {0: 640831, 1: 239169}, balance change: 4855.0
Step 880001: epsilon is now 0.0123
Starting episode 885001 Bet counts: {0: 645423, 1: 239577}, balance change: -1305.0
Step 885001: epsilon is now 0.0120
Starting episode 890001 Bet counts: {0: 649842, 1: 240158}, balance change: -24420.0
Step 890001: epsilon is now 0.0117
Starting episode 895001 Bet counts: {0: 654005, 1: 240995}, balance change: -2030.0
Step 895001: epsilon is now 0.0114
Starting episode 900001 Bet counts: {0: 658500, 1: 241500}, balance change: -12145.0
Step 900001: epsilon is now 0.0111
Starting episode 905001 Bet counts: {0: 663099, 1: 241901}, balance change: 8980.0
Step 905001: epsilon is now 0.0108
Starting episode 910001 Bet counts: {0: 667865, 1: 242135}, balance change: 5195.0
Step 910001: epsilon is now 0.0106
Starting episode 915001 Bet counts: {0: 672646, 1: 242354}, balance change: -100.0
Step 915001: epsilon is now 0.0103
Starting episode 920001 Bet counts: {0: 677312, 1: 242688}, balance change: -5695.0
Step 920001: epsilon is now 0.0101
Starting episode 925001 Bet counts: {0: 681935, 1: 243065}, balance change: 7970.0
Step 925001: epsilon is now 0.0098
Starting episode 930001 Bet counts: {0: 686630, 1: 243370}, balance change: 1830.0
Step 930001: epsilon is now 0.0096
Starting episode 935001 Bet counts: {0: 691316, 1: 243684}, balance change: 9805.0
Step 935001: epsilon is now 0.0093
Starting episode 940001 Bet counts: {0: 696040, 1: 243960}, balance change: 20830.0
Step 940001: epsilon is now 0.0091
Starting episode 945001 Bet counts: {0: 700831, 1: 244169}, balance change: -7780.0
Step 945001: epsilon is now 0.0089
Starting episode 950001 Bet counts: {0: 705571, 1: 244429}, balance change: 3515.0
Step 950001: epsilon is now 0.0087
Starting episode 955001 Bet counts: {0: 710393, 1: 244607}, balance change: 6685.0
Step 955001: epsilon is now 0.0084
Starting episode 960001 Bet counts: {0: 715196, 1: 244804}, balance change: 3385.0
Step 960001: epsilon is now 0.0082
Starting episode 965001 Bet counts: {0: 720039, 1: 244961}, balance change: 965.0
Step 965001: epsilon is now 0.0080
Starting episode 970001 Bet counts: {0: 724723, 1: 245277}, balance change: -5080.0
Step 970001: epsilon is now 0.0078
Starting episode 975001 Bet counts: {0: 729530, 1: 245470}, balance change: 7105.0
Step 975001: epsilon is now 0.0076
Starting episode 980001 Bet counts: {0: 734315, 1: 245685}, balance change: 8180.0
Step 980001: epsilon is now 0.0074
Starting episode 985001 Bet counts: {0: 739176, 1: 245824}, balance change: 6770.0
Step 985001: epsilon is now 0.0073
Starting episode 990001 Bet counts: {0: 744024, 1: 245976}, balance change: -2855.0
Step 990001: epsilon is now 0.0071
Starting episode 995001 Bet counts: {0: 748840, 1: 246160}, balance change: -11240.0
Step 995001: epsilon is now 0.0069
Agent 0 Win rate: 0.44, Win rate excluding ties: 0.49
Agent 0 Wins: 443970, losses: 465873, ties: 90157
Agent 0 Final balance: 200420.0
Device is cpu
Starting episode 1 Bet counts: {0: 0, 1: 0}, balance change: 0
Starting episode 5001 Bet counts: {0: 2509, 1: 2491}, balance change: -25040.0
Step 5001: epsilon is now 0.9753
Starting episode 10001 Bet counts: {0: 5051, 1: 4949}, balance change: -46575.0
Step 10001: epsilon is now 0.9512
Starting episode 15001 Bet counts: {0: 7546, 1: 7454}, balance change: 38495.0
Step 15001: epsilon is now 0.9277
Starting episode 20001 Bet counts: {0: 10022, 1: 9978}, balance change: -2125.0
Step 20001: epsilon is now 0.9048
Starting episode 25001 Bet counts: {0: 12497, 1: 12503}, balance change: 12855.0
Step 25001: epsilon is now 0.8825
Starting episode 30001 Bet counts: {0: 15026, 1: 14974}, balance change: -25110.0
Step 30001: epsilon is now 0.8607
Starting episode 35001 Bet counts: {0: 17613, 1: 17387}, balance change: 7425.0
Step 35001: epsilon is now 0.8395
Starting episode 40001 Bet counts: {0: 20205, 1: 19795}, balance change: -9635.0
Step 40001: epsilon is now 0.8187
Starting episode 45001 Bet counts: {0: 22743, 1: 22257}, balance change: 4860.0
Step 45001: epsilon is now 0.7985
Starting episode 50001 Bet counts: {0: 25379, 1: 24621}, balance change: 33670.0
Step 50001: epsilon is now 0.7788
Starting episode 55001 Bet counts: {0: 27862, 1: 27138}, balance change: 19990.0
Step 55001: epsilon is now 0.7596
Starting episode 60001 Bet counts: {0: 30382, 1: 29618}, balance change: 17370.0
Step 60001: epsilon is now 0.7408
Starting episode 65001 Bet counts: {0: 32927, 1: 32073}, balance change: -28815.0
Step 65001: epsilon is now 0.7225
Starting episode 70001 Bet counts: {0: 35431, 1: 34569}, balance change: -8615.0
Step 70001: epsilon is now 0.7047
Starting episode 75001 Bet counts: {0: 37939, 1: 37061}, balance change: 1120.0
Step 75001: epsilon is now 0.6873
Starting episode 80001 Bet counts: {0: 40488, 1: 39512}, balance change: -49265.0
Step 80001: epsilon is now 0.6703
Starting episode 85001 Bet counts: {0: 43075, 1: 41925}, balance change: -35955.0
Step 85001: epsilon is now 0.6538
Starting episode 90001 Bet counts: {0: 45383, 1: 44617}, balance change: -39220.0
Step 90001: epsilon is now 0.6376
Starting episode 95001 Bet counts: {0: 47758, 1: 47242}, balance change: -6615.0
Step 95001: epsilon is now 0.6219
Starting episode 100001 Bet counts: {0: 50052, 1: 49948}, balance change: -3465.0
Step 100001: epsilon is now 0.6065
Starting episode 105001 Bet counts: {0: 52754, 1: 52246}, balance change: -715.0
Step 105001: epsilon is now 0.5916
Starting episode 110001 Bet counts: {0: 55640, 1: 54360}, balance change: 1580.0
Step 110001: epsilon is now 0.5769
Starting episode 115001 Bet counts: {0: 58326, 1: 56674}, balance change: -40080.0
Step 115001: epsilon is now 0.5627
Starting episode 120001 Bet counts: {0: 60876, 1: 59124}, balance change: 6100.0
Step 120001: epsilon is now 0.5488
Starting episode 125001 Bet counts: {0: 63347, 1: 61653}, balance change: 43705.0
Step 125001: epsilon is now 0.5353
Starting episode 130001 Bet counts: {0: 65944, 1: 64056}, balance change: -15665.0
Step 130001: epsilon is now 0.5220
Starting episode 135001 Bet counts: {0: 68578, 1: 66422}, balance change: 21760.0
Step 135001: epsilon is now 0.5092
Starting episode 140001 Bet counts: {0: 70857, 1: 69143}, balance change: 42835.0
Step 140001: epsilon is now 0.4966
Starting episode 145001 Bet counts: {0: 73246, 1: 71754}, balance change: -29095.0
Step 145001: epsilon is now 0.4843
Starting episode 150001 Bet counts: {0: 75574, 1: 74426}, balance change: 18145.0
Step 150001: epsilon is now 0.4724
Starting episode 155001 Bet counts: {0: 77891, 1: 77109}, balance change: -8115.0
Step 155001: epsilon is now 0.4607
Starting episode 160001 Bet counts: {0: 80415, 1: 79585}, balance change: -6580.0
Step 160001: epsilon is now 0.4493
Starting episode 165001 Bet counts: {0: 82945, 1: 82055}, balance change: -14300.0
Step 165001: epsilon is now 0.4382
Starting episode 170001 Bet counts: {0: 85930, 1: 84070}, balance change: 35900.0
Step 170001: epsilon is now 0.4274
Starting episode 175001 Bet counts: {0: 88761, 1: 86239}, balance change: 16400.0
Step 175001: epsilon is now 0.4169
Starting episode 180001 Bet counts: {0: 91376, 1: 88624}, balance change: 53730.0
Step 180001: epsilon is now 0.4066
Starting episode 185001 Bet counts: {0: 93968, 1: 91032}, balance change: 9275.0
Step 185001: epsilon is now 0.3965
Starting episode 190001 Bet counts: {0: 96197, 1: 93803}, balance change: 23645.0
Step 190001: epsilon is now 0.3867
Starting episode 195001 Bet counts: {0: 98426, 1: 96574}, balance change: 28090.0
Step 195001: epsilon is now 0.3772
Starting episode 200001 Bet counts: {0: 100737, 1: 99263}, balance change: 54890.0
Step 200001: epsilon is now 0.3679
Starting episode 205001 Bet counts: {0: 103201, 1: 101799}, balance change: -20085.0
Step 205001: epsilon is now 0.3588
Starting episode 210001 Bet counts: {0: 105643, 1: 104357}, balance change: 5955.0
Step 210001: epsilon is now 0.3499
Starting episode 215001 Bet counts: {0: 107966, 1: 107034}, balance change: -21720.0
Step 215001: epsilon is now 0.3413
Starting episode 220001 Bet counts: {0: 110406, 1: 109594}, balance change: 8820.0
Step 220001: epsilon is now 0.3329
Starting episode 225001 Bet counts: {0: 112949, 1: 112051}, balance change: 39550.0
Step 225001: epsilon is now 0.3247
Starting episode 230001 Bet counts: {0: 115025, 1: 114975}, balance change: -29915.0
Step 230001: epsilon is now 0.3166
Starting episode 235001 Bet counts: {0: 116762, 1: 118238}, balance change: 22870.0
Step 235001: epsilon is now 0.3088
Starting episode 240001 Bet counts: {0: 118879, 1: 121121}, balance change: -28120.0
Step 240001: epsilon is now 0.3012
Starting episode 245001 Bet counts: {0: 120693, 1: 124307}, balance change: -5100.0
Step 245001: epsilon is now 0.2938
Starting episode 250001 Bet counts: {0: 122835, 1: 127165}, balance change: 13750.0
Step 250001: epsilon is now 0.2865
Starting episode 255001 Bet counts: {0: 125888, 1: 129112}, balance change: 18845.0
Step 255001: epsilon is now 0.2794
Starting episode 260001 Bet counts: {0: 128144, 1: 131856}, balance change: 11705.0
Step 260001: epsilon is now 0.2725
Starting episode 265001 Bet counts: {0: 130576, 1: 134424}, balance change: 13295.0
Step 265001: epsilon is now 0.2658
Starting episode 270001 Bet counts: {0: 132221, 1: 137779}, balance change: 3200.0
Step 270001: epsilon is now 0.2592
Starting episode 275001 Bet counts: {0: 134210, 1: 140790}, balance change: -3845.0
Step 275001: epsilon is now 0.2528
Starting episode 280001 Bet counts: {0: 136153, 1: 143847}, balance change: -38525.0
Step 280001: epsilon is now 0.2466
Starting episode 285001 Bet counts: {0: 138092, 1: 146908}, balance change: -36600.0
Step 285001: epsilon is now 0.2405
Starting episode 290001 Bet counts: {0: 139926, 1: 150074}, balance change: -34735.0
Step 290001: epsilon is now 0.2346
Starting episode 295001 Bet counts: {0: 141986, 1: 153014}, balance change: 15895.0
Step 295001: epsilon is now 0.2288
Starting episode 300001 Bet counts: {0: 143832, 1: 156168}, balance change: 305.0
Step 300001: epsilon is now 0.2231
Starting episode 305001 Bet counts: {0: 145693, 1: 159307}, balance change: 61775.0
Step 305001: epsilon is now 0.2176
Starting episode 310001 Bet counts: {0: 147354, 1: 162646}, balance change: -30290.0
Step 310001: epsilon is now 0.2122
Starting episode 315001 Bet counts: {0: 149431, 1: 165569}, balance change: 12030.0
Step 315001: epsilon is now 0.2070
Starting episode 320001 Bet counts: {0: 151217, 1: 168783}, balance change: 735.0
Step 320001: epsilon is now 0.2019
Starting episode 325001 Bet counts: {0: 153386, 1: 171614}, balance change: -23055.0
Step 325001: epsilon is now 0.1969
Starting episode 330001 Bet counts: {0: 155718, 1: 174282}, balance change: -9510.0
Step 330001: epsilon is now 0.1920
Starting episode 335001 Bet counts: {0: 157545, 1: 177455}, balance change: 10255.0
Step 335001: epsilon is now 0.1873
Starting episode 340001 Bet counts: {0: 159385, 1: 180615}, balance change: 15180.0
Step 340001: epsilon is now 0.1827
Starting episode 345001 Bet counts: {0: 161915, 1: 183085}, balance change: 22620.0
Step 345001: epsilon is now 0.1782
Starting episode 350001 Bet counts: {0: 163866, 1: 186134}, balance change: 18485.0
Step 350001: epsilon is now 0.1738
Starting episode 355001 Bet counts: {0: 166147, 1: 188853}, balance change: 3910.0
Step 355001: epsilon is now 0.1695
Starting episode 360001 Bet counts: {0: 168476, 1: 191524}, balance change: -24595.0
Step 360001: epsilon is now 0.1653
Starting episode 365001 Bet counts: {0: 170015, 1: 194985}, balance change: -12335.0
Step 365001: epsilon is now 0.1612
Starting episode 370001 Bet counts: {0: 171719, 1: 198281}, balance change: 40435.0
Step 370001: epsilon is now 0.1572
Starting episode 375001 Bet counts: {0: 173781, 1: 201219}, balance change: 795.0
Step 375001: epsilon is now 0.1534
Starting episode 380001 Bet counts: {0: 175670, 1: 204330}, balance change: -19855.0
Step 380001: epsilon is now 0.1496
Starting episode 385001 Bet counts: {0: 177560, 1: 207440}, balance change: -14410.0
Step 385001: epsilon is now 0.1459
Starting episode 390001 Bet counts: {0: 179295, 1: 210705}, balance change: 29675.0
Step 390001: epsilon is now 0.1423
Starting episode 395001 Bet counts: {0: 180974, 1: 214026}, balance change: -11415.0
Step 395001: epsilon is now 0.1388
Starting episode 400001 Bet counts: {0: 183682, 1: 216318}, balance change: 42825.0
Step 400001: epsilon is now 0.1353
Starting episode 405001 Bet counts: {0: 186134, 1: 218866}, balance change: -9195.0
Step 405001: epsilon is now 0.1320
Starting episode 410001 Bet counts: {0: 188383, 1: 221617}, balance change: -6360.0
Step 410001: epsilon is now 0.1287
Starting episode 415001 Bet counts: {0: 190460, 1: 224540}, balance change: -5470.0
Step 415001: epsilon is now 0.1256
Starting episode 420001 Bet counts: {0: 192864, 1: 227136}, balance change: 4505.0
Step 420001: epsilon is now 0.1225
Starting episode 425001 Bet counts: {0: 195368, 1: 229632}, balance change: 3180.0
Step 425001: epsilon is now 0.1194
Starting episode 430001 Bet counts: {0: 197422, 1: 232578}, balance change: 13520.0
Step 430001: epsilon is now 0.1165
Starting episode 435001 Bet counts: {0: 199478, 1: 235522}, balance change: 23910.0
Step 435001: epsilon is now 0.1136
Starting episode 440001 Bet counts: {0: 201864, 1: 238136}, balance change: 11255.0
Step 440001: epsilon is now 0.1108
Starting episode 445001 Bet counts: {0: 204204, 1: 240796}, balance change: -20465.0
Step 445001: epsilon is now 0.1081
Starting episode 450001 Bet counts: {0: 206726, 1: 243274}, balance change: -8725.0
Step 450001: epsilon is now 0.1054
Starting episode 455001 Bet counts: {0: 209327, 1: 245673}, balance change: -20780.0
Step 455001: epsilon is now 0.1028
Starting episode 460001 Bet counts: {0: 211934, 1: 248066}, balance change: -425.0
Step 460001: epsilon is now 0.1003
Starting episode 465001 Bet counts: {0: 214651, 1: 250349}, balance change: 26690.0
Step 465001: epsilon is now 0.0978
Starting episode 470001 Bet counts: {0: 217272, 1: 252728}, balance change: -855.0
Step 470001: epsilon is now 0.0954
Starting episode 475001 Bet counts: {0: 219504, 1: 255496}, balance change: 22470.0
Step 475001: epsilon is now 0.0930
Starting episode 480001 Bet counts: {0: 221777, 1: 258223}, balance change: 3765.0
Step 480001: epsilon is now 0.0907
Starting episode 485001 Bet counts: {0: 224226, 1: 260774}, balance change: -23715.0
Step 485001: epsilon is now 0.0885
Starting episode 490001 Bet counts: {0: 226809, 1: 263191}, balance change: -9805.0
Step 490001: epsilon is now 0.0863
Starting episode 495001 Bet counts: {0: 229028, 1: 265972}, balance change: 19180.0
Step 495001: epsilon is now 0.0842
Starting episode 500001 Bet counts: {0: 231144, 1: 268856}, balance change: -14945.0
Step 500001: epsilon is now 0.0821
Starting episode 505001 Bet counts: {0: 233116, 1: 271884}, balance change: -5465.0
Step 505001: epsilon is now 0.0801
Starting episode 510001 Bet counts: {0: 235627, 1: 274373}, balance change: 8030.0
Step 510001: epsilon is now 0.0781
Starting episode 515001 Bet counts: {0: 237635, 1: 277365}, balance change: 40370.0
Step 515001: epsilon is now 0.0762
Starting episode 520001 Bet counts: {0: 239690, 1: 280310}, balance change: 39290.0
Step 520001: epsilon is now 0.0743
Starting episode 525001 Bet counts: {0: 241867, 1: 283133}, balance change: 13620.0
Step 525001: epsilon is now 0.0724
Starting episode 530001 Bet counts: {0: 243957, 1: 286043}, balance change: 17345.0
Step 530001: epsilon is now 0.0707
Starting episode 535001 Bet counts: {0: 245817, 1: 289183}, balance change: -39865.0
Step 535001: epsilon is now 0.0689
Starting episode 540001 Bet counts: {0: 247972, 1: 292028}, balance change: -4600.0
Step 540001: epsilon is now 0.0672
Starting episode 545001 Bet counts: {0: 249820, 1: 295180}, balance change: -8280.0
Step 545001: epsilon is now 0.0655
Starting episode 550001 Bet counts: {0: 252083, 1: 297917}, balance change: -21970.0
Step 550001: epsilon is now 0.0639
Starting episode 555001 Bet counts: {0: 254144, 1: 300856}, balance change: 26550.0
Step 555001: epsilon is now 0.0623
Starting episode 560001 Bet counts: {0: 256424, 1: 303576}, balance change: 4865.0
Step 560001: epsilon is now 0.0608
Starting episode 565001 Bet counts: {0: 258844, 1: 306156}, balance change: 40170.0
Step 565001: epsilon is now 0.0593
Starting episode 570001 Bet counts: {0: 261393, 1: 308607}, balance change: 38705.0
Step 570001: epsilon is now 0.0578
Starting episode 575001 Bet counts: {0: 263384, 1: 311616}, balance change: 41830.0
Step 575001: epsilon is now 0.0564
Starting episode 580001 Bet counts: {0: 265372, 1: 314628}, balance change: 9660.0
Step 580001: epsilon is now 0.0550
Starting episode 585001 Bet counts: {0: 267758, 1: 317242}, balance change: 30030.0
Step 585001: epsilon is now 0.0537
Starting episode 590001 Bet counts: {0: 269769, 1: 320231}, balance change: -27560.0
Step 590001: epsilon is now 0.0523
Starting episode 595001 Bet counts: {0: 271917, 1: 323083}, balance change: 30265.0
Step 595001: epsilon is now 0.0510
Starting episode 600001 Bet counts: {0: 273918, 1: 326082}, balance change: 37950.0
Step 600001: epsilon is now 0.0498
Starting episode 605001 Bet counts: {0: 276157, 1: 328843}, balance change: -4870.0
Step 605001: epsilon is now 0.0486
Starting episode 610001 Bet counts: {0: 278271, 1: 331729}, balance change: 5590.0
Step 610001: epsilon is now 0.0474
Starting episode 615001 Bet counts: {0: 280955, 1: 334045}, balance change: 20185.0
Step 615001: epsilon is now 0.0462
Starting episode 620001 Bet counts: {0: 283338, 1: 336662}, balance change: -25610.0
Step 620001: epsilon is now 0.0450
Starting episode 625001 Bet counts: {0: 285865, 1: 339135}, balance change: 6035.0
Step 625001: epsilon is now 0.0439
Starting episode 630001 Bet counts: {0: 288404, 1: 341596}, balance change: 38725.0
Step 630001: epsilon is now 0.0429
Starting episode 635001 Bet counts: {0: 291000, 1: 344000}, balance change: -22550.0
Step 635001: epsilon is now 0.0418
Starting episode 640001 Bet counts: {0: 294026, 1: 345974}, balance change: -1225.0
Step 640001: epsilon is now 0.0408
Starting episode 645001 Bet counts: {0: 296685, 1: 348315}, balance change: 35830.0
Step 645001: epsilon is now 0.0398
Starting episode 650001 Bet counts: {0: 299368, 1: 350632}, balance change: 23830.0
Step 650001: epsilon is now 0.0388
Starting episode 655001 Bet counts: {0: 302307, 1: 352693}, balance change: -10775.0
Step 655001: epsilon is now 0.0378
Starting episode 660001 Bet counts: {0: 304911, 1: 355089}, balance change: -22720.0
Step 660001: epsilon is now 0.0369
Starting episode 665001 Bet counts: {0: 307774, 1: 357226}, balance change: 6690.0
Step 665001: epsilon is now 0.0360
Starting episode 670001 Bet counts: {0: 310395, 1: 359605}, balance change: 31060.0
Step 670001: epsilon is now 0.0351
Starting episode 675001 Bet counts: {0: 313203, 1: 361797}, balance change: -19070.0
Step 675001: epsilon is now 0.0342
Starting episode 680001 Bet counts: {0: 315485, 1: 364515}, balance change: 49355.0
Step 680001: epsilon is now 0.0334
Starting episode 685001 Bet counts: {0: 318065, 1: 366935}, balance change: 28225.0
Step 685001: epsilon is now 0.0325
Starting episode 690001 Bet counts: {0: 321055, 1: 368945}, balance change: -13130.0
Step 690001: epsilon is now 0.0317
Starting episode 695001 Bet counts: {0: 324165, 1: 370835}, balance change: -11970.0
Step 695001: epsilon is now 0.0310
Starting episode 700001 Bet counts: {0: 326517, 1: 373483}, balance change: 23975.0
Step 700001: epsilon is now 0.0302
Starting episode 705001 Bet counts: {0: 329316, 1: 375684}, balance change: -1070.0
Step 705001: epsilon is now 0.0295
Starting episode 710001 Bet counts: {0: 331938, 1: 378062}, balance change: -5855.0
Step 710001: epsilon is now 0.0287
Starting episode 715001 Bet counts: {0: 334588, 1: 380412}, balance change: -240.0
Step 715001: epsilon is now 0.0280
Starting episode 720001 Bet counts: {0: 337200, 1: 382800}, balance change: -23220.0
Step 720001: epsilon is now 0.0273
Starting episode 725001 Bet counts: {0: 340134, 1: 384866}, balance change: -12910.0
Step 725001: epsilon is now 0.0266
Starting episode 730001 Bet counts: {0: 342906, 1: 387094}, balance change: 15190.0
Step 730001: epsilon is now 0.0260
Starting episode 735001 Bet counts: {0: 345646, 1: 389354}, balance change: 18240.0
Step 735001: epsilon is now 0.0253
Starting episode 740001 Bet counts: {0: 348528, 1: 391472}, balance change: -31115.0
Step 740001: epsilon is now 0.0247
Starting episode 745001 Bet counts: {0: 350992, 1: 394008}, balance change: -41795.0
Step 745001: epsilon is now 0.0241
Starting episode 750001 Bet counts: {0: 353353, 1: 396647}, balance change: 18960.0
Step 750001: epsilon is now 0.0235
Starting episode 755001 Bet counts: {0: 355966, 1: 399034}, balance change: -8975.0
Step 755001: epsilon is now 0.0229
Starting episode 760001 Bet counts: {0: 358272, 1: 401728}, balance change: 33780.0
Step 760001: epsilon is now 0.0224
Starting episode 765001 Bet counts: {0: 360790, 1: 404210}, balance change: 18310.0
Step 765001: epsilon is now 0.0218
Starting episode 770001 Bet counts: {0: 362923, 1: 407077}, balance change: -4580.0
Step 770001: epsilon is now 0.0213
Starting episode 775001 Bet counts: {0: 364810, 1: 410190}, balance change: -43190.0
Step 775001: epsilon is now 0.0208
Starting episode 780001 Bet counts: {0: 367318, 1: 412682}, balance change: 22515.0
Step 780001: epsilon is now 0.0202
Starting episode 785001 Bet counts: {0: 369756, 1: 415244}, balance change: 2655.0
Step 785001: epsilon is now 0.0197
Starting episode 790001 Bet counts: {0: 372090, 1: 417910}, balance change: 21735.0
Step 790001: epsilon is now 0.0193
Starting episode 795001 Bet counts: {0: 374777, 1: 420223}, balance change: 18620.0
Step 795001: epsilon is now 0.0188
Starting episode 800001 Bet counts: {0: 377381, 1: 422619}, balance change: 12390.0
Step 800001: epsilon is now 0.0183
Starting episode 805001 Bet counts: {0: 379911, 1: 425089}, balance change: -1025.0
Step 805001: epsilon is now 0.0179
Starting episode 810001 Bet counts: {0: 382301, 1: 427699}, balance change: 12000.0
Step 810001: epsilon is now 0.0174
Starting episode 815001 Bet counts: {0: 384886, 1: 430114}, balance change: 2495.0
Step 815001: epsilon is now 0.0170
Starting episode 820001 Bet counts: {0: 387657, 1: 432343}, balance change: 48360.0
Step 820001: epsilon is now 0.0166
Starting episode 825001 Bet counts: {0: 390097, 1: 434903}, balance change: 19945.0
Step 825001: epsilon is now 0.0162
Starting episode 830001 Bet counts: {0: 392237, 1: 437763}, balance change: -35505.0
Step 830001: epsilon is now 0.0158
Starting episode 835001 Bet counts: {0: 394762, 1: 440238}, balance change: 16505.0
Step 835001: epsilon is now 0.0154
Starting episode 840001 Bet counts: {0: 396861, 1: 443139}, balance change: 35175.0
Step 840001: epsilon is now 0.0150
Starting episode 845001 Bet counts: {0: 399561, 1: 445439}, balance change: -14210.0
Step 845001: epsilon is now 0.0146
Starting episode 850001 Bet counts: {0: 402142, 1: 447858}, balance change: -60235.0
Step 850001: epsilon is now 0.0143
Starting episode 855001 Bet counts: {0: 404552, 1: 450448}, balance change: -59495.0
Step 855001: epsilon is now 0.0139
Starting episode 860001 Bet counts: {0: 406618, 1: 453382}, balance change: 21855.0
Step 860001: epsilon is now 0.0136
Starting episode 865001 Bet counts: {0: 408962, 1: 456038}, balance change: -3355.0
Step 865001: epsilon is now 0.0132
Starting episode 870001 Bet counts: {0: 410929, 1: 459071}, balance change: -19740.0
Step 870001: epsilon is now 0.0129
Starting episode 875001 Bet counts: {0: 413331, 1: 461669}, balance change: -7755.0
Step 875001: epsilon is now 0.0126
Starting episode 880001 Bet counts: {0: 415476, 1: 464524}, balance change: 36850.0
Step 880001: epsilon is now 0.0123
Starting episode 885001 Bet counts: {0: 417810, 1: 467190}, balance change: 18250.0
Step 885001: epsilon is now 0.0120
Starting episode 890001 Bet counts: {0: 420131, 1: 469869}, balance change: -3215.0
Step 890001: epsilon is now 0.0117
Starting episode 895001 Bet counts: {0: 422053, 1: 472947}, balance change: 12000.0
Step 895001: epsilon is now 0.0114
Starting episode 900001 Bet counts: {0: 424080, 1: 475920}, balance change: 63075.0
Step 900001: epsilon is now 0.0111
Starting episode 905001 Bet counts: {0: 426163, 1: 478837}, balance change: -21450.0
Step 905001: epsilon is now 0.0108
Starting episode 910001 Bet counts: {0: 428080, 1: 481920}, balance change: -10115.0
Step 910001: epsilon is now 0.0106
Starting episode 915001 Bet counts: {0: 430111, 1: 484889}, balance change: 4390.0
Step 915001: epsilon is now 0.0103
Starting episode 920001 Bet counts: {0: 432385, 1: 487615}, balance change: -30160.0
Step 920001: epsilon is now 0.0101
Starting episode 925001 Bet counts: {0: 434262, 1: 490738}, balance change: -7740.0
Step 925001: epsilon is now 0.0098
Starting episode 930001 Bet counts: {0: 435984, 1: 494016}, balance change: -1340.0
Step 930001: epsilon is now 0.0096
Starting episode 935001 Bet counts: {0: 437773, 1: 497227}, balance change: 33680.0
Step 935001: epsilon is now 0.0093
Starting episode 940001 Bet counts: {0: 439507, 1: 500493}, balance change: -6285.0
Step 940001: epsilon is now 0.0091
Starting episode 945001 Bet counts: {0: 441661, 1: 503339}, balance change: -1830.0
Step 945001: epsilon is now 0.0089
Starting episode 950001 Bet counts: {0: 444028, 1: 505972}, balance change: -14360.0
Step 950001: epsilon is now 0.0087
Starting episode 955001 Bet counts: {0: 446212, 1: 508788}, balance change: 3195.0
Step 955001: epsilon is now 0.0084
Starting episode 960001 Bet counts: {0: 448355, 1: 511645}, balance change: -28845.0
Step 960001: epsilon is now 0.0082
Starting episode 965001 Bet counts: {0: 450259, 1: 514741}, balance change: -7825.0
Step 965001: epsilon is now 0.0080
Starting episode 970001 Bet counts: {0: 452557, 1: 517443}, balance change: 30170.0
Step 970001: epsilon is now 0.0078
Starting episode 975001 Bet counts: {0: 454296, 1: 520704}, balance change: -40390.0
Step 975001: epsilon is now 0.0076
Starting episode 980001 Bet counts: {0: 456652, 1: 523348}, balance change: 14565.0
Step 980001: epsilon is now 0.0074
Starting episode 985001 Bet counts: {0: 458914, 1: 526086}, balance change: -115.0
Step 985001: epsilon is now 0.0073
Starting episode 990001 Bet counts: {0: 461004, 1: 528996}, balance change: -3055.0
Step 990001: epsilon is now 0.0071
Starting episode 995001 Bet counts: {0: 463248, 1: 531752}, balance change: -1950.0
Step 995001: epsilon is now 0.0069
Agent 1 Win rate: 0.44, Win rate excluding ties: 0.49
Agent 1 Wins: 443935, losses: 464831, ties: 91234
Agent 1 Final balance: 553815.0
Mean win rate: 0.44, Mean win rate excluding ties: 0.49
Mean cumulative rewards: -21399.5
Bet counts 0: 465641 and 1: 534359
Program completed successfully.
python3 driver.py -e 1000000 -t q-learning -b dqn -a 2  5339.00s user 12988.16s system 199% cpu 2:33:09.66 total
(aaml-final) ➜  code git:(main) ✗
