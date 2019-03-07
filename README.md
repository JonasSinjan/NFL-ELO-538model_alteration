# NFLprediction
Made a slight alteration to 538's NFL ELO prediction model:
Used each team's home field win percentage as their home field advantage term instead of a global 65

Also only used data from Superbowl era.
From which: My forecasts would have gotten 847.88 points per season. Elo got 841.85 points per season.

2018 season results
For regular season 538's model performed better.
But for playoff games my model performed better.

My model 2018 results: 723.7 points per season.
538 Elo got 718.9 points per season.

The code at the moment hasn't been tidied up so there is a small bug: to run must set updatebool in line 25 of run.py to True, run again with it set to False. 

This model predicts a team winning its game the following week.  During the Offseason, which it is currently at the time or writing, the model doesn't function.
