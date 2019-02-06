from util import *
from forecast import *

listofteams = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX',
               'KC', 'LAC', 'LAR', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SEA', 'SF', 'TB',
               'TEN', 'WSH']
Forecastbool = False
# working out HFA for each team from 1966 data till 2017
if Forecastbool == False:
    games = Util.read_games("nfl_games_mod.csv", False)
    homewins, totalgames, homewinpercentage = Util.HFAlist(games, listofteams)
    roundedHFA = [round(x, 2) for x in homewinpercentage]
    # print(roundedHFA)
    avgHFA = sum(roundedHFA) / len(roundedHFA)
    # print(avgHFA)
    HFAlist = roundedHFA
    HFA = 65
    K = 20
    Forecast.forecast(games, HFA, K, False, True, roundedHFA, listofteams)
    Util.evaluate_forecasts(games)

Forecastbool = True
# now just forecasting the upcoming games and working out model would have done this season compared to 538 elo
if Forecastbool == True:
    games = Util.read_games("nfl_games_2018.csv",False)  # must update games every week tho, so once a week run program with updatebool set to True
    # update will print out predictions twice and work out points for season twice and add, not sure why this bug happens but once updated set bool back to false and this will no longer happen
    HFA = 65
    K = 20
    Forecast.forecast(games, HFA, K, False, True, roundedHFA, listofteams)
    Util.evaluate_forecasts(games)


# for x in HFA_alt:
#     Forecast.forecast(games,HFA,K,x)
#     Util.evaluate_forecasts(games)
#     print("FHA= %s, K=%s, FHA_alt = %s" % (HFA, K, x))
# # Evaluate our forecasts against Elo

# if true I get 824.4 points per season-still lower than 826.63 but better than whatever I have that only gets 821.01
# for i in range(len(fhalist)):
# FHA = fhalist[i]
# print(FHA)
# Forecast.forecast(games,HFA,K,False,roundedHFA, listofteams)
# Util.evaluate_forecasts(games)
# now 66 or 59 is better number and i removed the hfa per teams and get a lower number than elo-they should now both be getting the same number-when only considering superbowl era matches-1996 and beyond
# 66 is greater 639.07
# 70 also 639.12
# currently max is 641.03 points per season doing top 10 teams individually and setting HFA to 57 overall
