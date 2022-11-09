import requests
import json
from mysql.connector import connect, errors, errorcode
from congif import host, user, password, db_name


def get_league_ids():
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        print(f'Successfully connected to {db_name} database.')

        select_league_ids_query = 'SELECT league_id FROM tracked_tournaments'
        league_ids = []

        try:
            with connection.cursor() as cursor:
                cursor.execute(select_league_ids_query)
                for each in cursor.fetchall():
                    league_ids.append(each[0])
        except errors.Error as err:
            print('Unexpected error', err, errorcode)
        finally:
            connection.close()
            print('League IDs fetched, closing connection.')
            return league_ids

    except errors.Error as err:
        print('Connection refused.')
        print(err, errorcode)


league_ids = get_league_ids()

for l_id in league_ids:
    payload = {'league_id': l_id, 'key': 'D102CBA62E2B251B48F5C2D46E736888'}
    r = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/', params=payload)

    data = r.json()
    live_games = len(data['result']['games'])


    for game in range(live_games):
        league_id = data['result']['games'][game]['league_id']
        match_id = data['result']['games'][game]['match_id']
        radiant_team = {
            "team_name": data['result']['games'][game]['radiant_team']['team_name'],
            "team_id": data['result']['games'][game]['radiant_team']['team_id']
        }
        dire_team = {
            "team_name": data['result']['games'][game]['dire_team']['team_name'],
            "team_id": data['result']['games'][game]['dire_team']['team_id']
        }
        radiant_series_wins = data['result']['games'][game]['radiant_series_wins']
        dire_series_wins = data['result']['games'][game]['dire_series_wins']

        radiant_pick = []
        dire_pick = []
        picks = data['result']['games'][game]['players']

        for i in picks:
            if i['team'] == 0:
                radiant_pick.append(i['hero_id'])
            elif i['team'] == 1:
                dire_pick.append(i['hero_id'])

        game = {
            "league_id": league_id,
            "match_id": match_id,
            "radiant_team": {
                "team_name": radiant_team['team_name'],
                "team_id": radiant_team['team_id']
            },
            "dire_team": {
                "team_name": dire_team['team_name'],
                "team_id": dire_team['team_id']
            },
            # Пока что все, что связано с серией не нужно, так как в первую очередь
            # буду делать по картам
            # "radiant_series_wins": radiant_series_wins,
            # "dire_series_wins": dire_series_wins,
            "picks": {
                "radiant": radiant_pick,
                "dire": dire_pick
            }
        }

        print(json.dumps(game, indent=4))

# data > result > games(list) > radiant_team > team_name, team_id
# data > result > games(list) > dire_team > team_name, team_id
# data > result > games(list) > match_id
# data > result > games(list) > league_id
# data > result > games(list) > radiant_series_wins
# data > result > games(list) > dire_series_wins
# data > result > games(list) > players(list) >
# team (0 - radiant, 1 - dire), hero_id



# Есть список league_id из ДБ
# Делаем запрос лайв игр на каждую league_id в цикле
# Узнаем сколько игр идет на текущий момент - len(data['result']['games'])
# Проходим в цикле по каждой игре, получая необходимую информацию


# ЧТО НУЖНО СОХРАНЯТЬ В ДБ

# MAP_INFO: league_id, match_id, radiant_team_name, radiant_team_id, dire_team_name, dire_team_id, winner
# PICKS: league_id, match_id, hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10,
