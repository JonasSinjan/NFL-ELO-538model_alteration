# NFLprediction - 538 ELO model

The main goal for this exercise was to go through and understand an elo model written by someone else and gain experience tinkering with prediction models.  This experience taught me good coding habits, eg: how to setup different python files and execute in one main run.py. It also exposed to the use of staticmethods within classes.

Made a slight alteration to 538's NFL ELO prediction model:
Used each team's home field win percentage as their home field advantage term instead of a global 65

Also only used data from Superbowl era.
From which: My forecasts would have gotten 847.88 points per season. Elo got 841.85 points per season.

2018 season results
For regular season 538's model performed better.
But for playoff games my model performed better. (538's forecasting game weights playoff games twice as much as regular season games)

My model 2018 results: 723.7 points per season.
538 Elo got 718.9 points per season.

Overall very little difference, this difference is well within the standard deviation of the original model.  Shows that it is pretty accurate to use a global home field advantage term. 

The code at the moment hasn't been tidied up so there is a small bug: to run must set updatebool in line 25 of run.py to True, run again with it set to False. 

This model predicts a team winning its game the following week.  During the Offseason, which it is currently at the time of writing, there are bugs that need to be fixed at a later date.
