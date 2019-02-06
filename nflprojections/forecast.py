import csv
import math

HFA = 65.0  # Home field advantage is worth 65 Elo points
K = 20.0  # The speed at which Elo ratings change
REVERT = 1 / 3.0  # Between seasons, a team retains 2/3 of its previous season's rating

REVERSIONS = {'CBD1925': 1502.032, 'RAC1926': 1403.384, 'LOU1926': 1307.201, 'CIB1927': 1362.919, 'MNN1929': 1306.702,
              # Some between-season reversions of unknown origin
              'BFF1929': 1331.943, 'LAR1944': 1373.977, 'PHI1944': 1497.988, 'ARI1945': 1353.939, 'PIT1945': 1353.939,
              'CLE1999': 1300.0}


class Forecast:

    @staticmethod
    def forecast(games, HFA, K, oldindividualHFA, calculatedHFA, roundedHFA, listofteams):
        #oldindividualHFA is a boolean to denote whether to use HFA from all years
        #calculated HFA is a booleanto denote whether to use HFA calculated from 1966 data onwards
        #roundedHFA = list that contains 1966 calculated HFA
        """ Generates win probabilities in the my_prob1 field for each game based on Elo model """

        # Initialize team objects to maintain ratings
        teams = {}
        for row in [item for item in csv.DictReader(open("initial_elos.csv"))]:
            teams[row['team']] = {
                'name': row['team'],
                'season': None,
                'elo': float(row['elo'])
            }

        for game in games:
            team1, team2 = teams[game['team1']], teams[game['team2']]
            if game['elo_prob1'] == None :
                continue
            elo1, elo2 = game['elo1'], game['elo2']
            # Revert teams at the start of seasons
            for team in [team1, team2]:
                if team['season'] and game['season'] != team['season']:
                    k = "%s%s" % (team['name'], game['season'])
                    if k in REVERSIONS:
                        team['elo'] = REVERSIONS[k]
                    else:
                        team['elo'] = 1505.0 * REVERT + team['elo'] * (1 - REVERT)
                team['season'] = game['season']

            # Elo difference includes home field advantage
            #for top 6 teams with higher than expected home field win rates
            #if team1['name'] == 'DEN' or team1['name'] == 'NE' or team1['name'] == 'GB' or team1['name']=='BAL' or team1['name'] == 'PIT':
             #   elo_diff = team1['elo'] - team2['elo'] + (0 if game['neutral'] == 1 else HFA_alt)
            if oldindividualHFA == True:
                if team1['name']=='DEN':
                    HFA_den = 73
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_den)
                elif team1['name']=='NE':
                    HFA_ne = 71
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_ne)
                elif team1['name']=='BAL':
                    HFA_bal = 69
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_bal)
                elif team1['name']=='PIT':
                    HFA_pit = 69
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_pit)
                elif team1['name']=='GB':
                    HFA_gb = 68
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_gb)
                elif team1['name'] == 'MIN':
                    HFA_min = 66
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_min)
                elif team1['name'] == 'SF':
                    HFA_sf= 65
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_sf)
                elif team1['name'] == 'SEA':
                    HFA_sea = 64
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_sea)
                elif team1['name'] == 'KC':
                    HFA_kc = 63
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_kc)
                elif team1['name'] == 'PHI':
                    HFA_phi = 61
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_phi)
                elif team1['name'] == 'BUF':
                    HFA_buf = 60
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_buf)
                elif team1['name'] == 'MIA':
                    HFA_mia = 60
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_mia)
                elif team1['name'] == 'IND':
                    HFA_ind = 59
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_ind)
                elif team1['name'] == 'DAL':
                    HFA_dal = 59
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_dal)
                elif team1['name'] == 'NYG':
                    HFA_nyg = 59
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_nyg)
                elif team1['name'] == 'CHI':
                    HFA_chi = 58
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_chi)
                elif team1['name'] == 'TEN':
                    HFA_ten = 58
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_ten)
                elif team1['name'] == 'CAR':
                    HFA_car = 56
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_car)
                elif team1['name'] == 'NO':
                    HFA_no = 55
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_no)
                elif team1['name'] == 'ATL':
                    HFA_atl = 55
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_atl)
                elif team1['name'] == 'WSH':
                    HFA_wsh = 55
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_wsh)
                elif team1['name'] == 'JAX':
                    HFA_jax = 55
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_jax)
                elif team1['name'] == 'LAC':
                    HFA_lac = 54
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_lac)
                elif team1['name'] == 'CIN':
                    HFA_cin = 53
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_cin)
                elif team1['name'] == 'ARI':
                    HFA_ari = 52
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_ari)
                elif team1['name'] == 'HOU':
                    HFA_hou = 52
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_hou)
                elif team1['name'] == 'NYJ':
                    HFA_nyj = 51
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_nyj)
                elif team1['name'] == 'OAK':
                    HFA_oak = 51
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_oak)
                elif team1['name'] == 'DET':
                    HFA_det = 50
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_det)
                elif team1['name'] == 'LAR':
                    HFA_lar = 49
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_lar)
                elif team1['name'] == 'TB':
                    HFA_tb = 48
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_tb)
                elif team1['name'] == 'CLE':
                    HFA_cle = 43
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA_cle)
                else:
                    elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA)

            elif calculatedHFA == True:
                index = listofteams.index(game['team1'])
                HFA = roundedHFA[index]
                elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA)

            else:
                elo_diff = float(elo1) - float(elo2) + (0 if game['neutral'] == 1 else HFA)

            # This is the most important piece, where we set my_prob1 to our forecasted probability
            if game['elo_prob1'] != None:
                game['my_prob1'] = 1.0 / (math.pow(10.0, (-elo_diff / 400.0)) + 1.0)
                # problist.append(game['my_prob1'])

            # If game was played, maintain team Elo ratings
            if game['score1'] != None:
                # what is result, its not the score, is a result of 1 = a win? and a result of 0.5=draw?
                # Margin of victory is used as a K multiplier
                pd = abs(game['score1'] - game['score2'])
                mult = math.log(max(pd, 1) + 1.0) * (2.2 / (1.0 if game['result1'] == 0.5 else (
                            (elo_diff if game['result1'] == 1.0 else -elo_diff) * 0.001 + 2.2)))
                # wonder where the 2.2, 1, 0.001,2.2 numbers all come from, also ln() why?
                #this is the autocorrelation problem
                # want to know why the formula for the prob is what it is
                # Elo shift based on K and the margin of victory multiplier
                shift = (K * mult) * (game['result1'] - game['my_prob1'])

                # Apply shift
                team1['elo'] += shift
                team2['elo'] -= shift


