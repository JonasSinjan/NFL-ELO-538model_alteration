import csv
import numpy as np

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


class Util:

    @staticmethod
    def read_games(file, updatebool):
        """ Initializes game objects from csv """
        games = [item for item in csv.DictReader(open(file))]

        # Uncommenting these three lines will grab the latest game results for 2018, update team ratings accordingly, and make forecasts for upcoming games
        # comment these if finding out how model is doing this season cos otherwise will add it twice and clash as file wont have _mod
        # file_2018 = file.replace("_mod.", "_2018.")
        if updatebool == True: #to update the 2018 file with latest results and make most accurate predictions
            file_2018 = file  # run these last three to update the 2018 file with latest results
            urlretrieve("https://projects.fivethirtyeight.com/nfl-api/2018/nfl_games_2018.csv", file_2018)
            games += [item for item in csv.DictReader(open(file_2018))]

        for game in games:
            game['season'], game['neutral'], game['playoff'] = int(game['season']), int(game['neutral']), int(
                game['playoff'])
            game['score1'], game['score2'] = int(game['score1']) if game['score1'] != '' else None, int(
                game['score2']) if game['score2'] != '' else None
            game['elo_prob1'], game['result1'] = float(game['elo_prob1']) if game['elo_prob1'] != '' else None, float(
                game['result1']) if game['result1'] != '' else None

        return games

    def HFAlist(games, listofteams):  # only if on mod game file #where the actual home win percentage from the file is calculated
        homewins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        totalgames = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for game in games:
            if game['result1'] != None:
                # print(game['team1'])
                # print(type(game['team1']))
                team = game['team1']
                # print(type(team))
                # print(team)
                index = listofteams.index(team)
                # print(index)
                # print(type(index))
                totalgames[index] += 1
                # print(totalgames[index])
                if game['result1'] == 1:
                    homewins[index] += 1
                    # print(homewins[index])
                else:
                    continue
        homewinpercentage = [100 * x / y for x, y in zip(homewins, totalgames)]
        return homewins, totalgames, homewinpercentage

    @staticmethod
    def evaluate_forecasts(games):
        """ Evaluates and scores forecasts in the my_prob1 field against those in the elo_prob1 field for each game """
        my_points_by_season, elo_points_by_season = {}, {}
        problist = []
        forecasted_games = [g for g in games if g['result1'] != None]
        upcoming_games = [g for g in games if g['result1'] == None and 'my_prob1' in g]
        # print(upcoming_games)
        i = 0
        # Evaluate forecasts and group by season
        for game in forecasted_games:
            i += 1
            # print(i)
            # Skip unplayed games and ties
            if game['result1'] == None or game['result1'] == 0.5:
                problist.append(round(game['my_prob1'], 2))
                problist.append(round(game['elo_prob1'], 2))

                continue

            if game['season'] not in elo_points_by_season:
                elo_points_by_season[game['season']] = 0.0
                my_points_by_season[game['season']] = 0.0

            # Calculate elo's points for game
            rounded_elo_prob = round(game['elo_prob1'], 2)
            elo_brier = (rounded_elo_prob - game['result1']) * (rounded_elo_prob - game['result1'])
            elo_points = 25 - (100 * elo_brier)
            elo_points = round(elo_points + 0.001 if elo_points < 0 else elo_points, 1)  # Round half up
            if game['playoff'] == 1:
                elo_points *= 2
            elo_points_by_season[game['season']] += elo_points

            # Calculate my points for game
            rounded_my_prob = round(game['my_prob1'], 2)
            problist.append(rounded_my_prob)
            problist.append(rounded_elo_prob)
            my_brier = (rounded_my_prob - game['result1']) * (rounded_my_prob - game['result1'])
            my_points = 25 - (100 * my_brier)
            my_points = round(my_points + 0.001 if my_points < 0 else my_points, 1)  # Round half up
            if game['playoff'] == 1:
                my_points *= 2
            my_points_by_season[game['season']] += my_points

        # Print individual seasons
        # for season in my_points_by_season:
        #   print("In %s, your forecasts would have gotten %s points. Elo got %s points." % (season, round(my_points_by_season[season], 2), round(elo_points_by_season[season], 2)))

        # Show overall performance
        my_avg = sum(my_points_by_season.values()) / len(my_points_by_season.values())
        # print(len(my_points_by_season.values()))
        elo_avg = sum(elo_points_by_season.values()) / len(elo_points_by_season.values())
        print("\nOn average, your forecasts would have gotten %s points per season. Elo got %s points per season.\n" % (
        round(my_avg, 2), round(elo_avg, 2)))
        a = np.array(problist)
        length = len(problist)
        columns = length / 2
        avert = a.reshape(int(columns), 2)
        # print(avert)

        # Print forecasts for upcoming games
        if len(upcoming_games) > 0:
            print("Forecasts for upcoming games:")
            for game in upcoming_games:
                print("%s\t%s vs. %s\t\t%s%% (Elo)\t\t%s%% (You)" % (
                game['date'], game['team1'], game['team2'], int(round(100 * game['elo_prob1'])),
                int(round(100 * game['my_prob1']))))
            print("")
