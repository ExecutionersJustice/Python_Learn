import requests
import json
from mysql.connector import connect, errors, errorcode
from congif import host, user, password, db_name
from datetime import datetime

tournaments_query = """{  
  leagues(request: 
    {take: 100, 
    tiers: [INTERNATIONAL, 
            MAJOR, 
            MINOR, 
            PROFESSIONAL, 
            DPC_LEAGUE, 
            DPC_QUALIFIER, 
            DPC_LEAGUE_FINALS, 
            DPC_LEAGUE_QUALIFIER], 
    isFutureLeague:false, 
    leagueEnded:false}) {  
        displayName  
        id  
        startDateTime 
        endDateTime 
  }  
}"""

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiJodHRwczovL3N0ZWFtY29tbXVuaXR5LmNvbS9vcGVuaWQvaWQvNzY1NjExOTg5OTI3MTU4NDAiLCJ1bmlxdWVfbmFtZSI6IlRpbWUiLCJTdWJqZWN0IjoiN2RjMWI4MmEtMzQzMy00MGJkLWJhYzgtYzRlYWE1NjM1MzU1IiwiU3RlYW1JZCI6IjEwMzI0NTAxMTIiLCJuYmYiOjE2NjU3NzY4NDcsImV4cCI6MTY5NzMxMjg0NywiaWF0IjoxNjY1Nzc2ODQ3LCJpc3MiOiJodHRwczovL2FwaS5zdHJhdHouY29tIn0.JclJ_IRoAgFVnQJ9FFacSdozF2yP-YEEGFrZdGvY_Tc'
headers = {"Authorization": f"Bearer {token}"}


url = 'https://api.stratz.com/graphql'
response = requests.post(url, json={'query': tournaments_query}, headers=headers)
data = response.json()


print(f'RESPONSE STATUS: {response.status_code}')
print('........................................................................................................')


tracked_tournaments = []
untracked_tournaments = []

try:
    connection = connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print(f'Successfully connected to {db_name} database.')

    for i in data['data']['leagues']:
        name = i['displayName']
        id = i['id']
        startTime = datetime.utcfromtimestamp(i['startDateTime']).strftime('%Y-%m-%d %H:%M:%S')
        endTime = datetime.utcfromtimestamp(i['endDateTime']).strftime('%Y-%m-%d %H:%M:%S')


        user_input = input(f'Tournament: {i["displayName"]}. Do you want to track it? Y/N: ').upper()

        if user_input == 'Y':
            tracked_tournaments.append([id, name, startTime, endTime])

        elif user_input == 'N':
            untracked_tournaments.append([id, name, startTime, endTime])

    try:
        insert_tracked_tournaments_query = f'''
                INSERT IGNORE INTO tracked_tournaments
                (league_id, league_name, start_date_time, end_date_time)
                VALUES (%s, %s, %s, %s)
                '''
        with connection.cursor() as cursor:
            cursor.executemany(insert_tracked_tournaments_query, tuple(tracked_tournaments))
            connection.commit()
    except errors.Error as err:
        print('Data was not inserted\n', errorcode, err)

    try:
        insert_untracked_tournaments_query = f'''
                 INSERT IGNORE INTO untracked_tournaments
                 (league_id, league_name, start_date_time, end_date_time)
                 VALUES (%s, %s, %s, %s)
                 '''
        with connection.cursor() as cursor:
            cursor.executemany(insert_untracked_tournaments_query, tuple(untracked_tournaments))
            connection.commit()
    except errors.Error as err:
        print('Data was not inserted\n', errorcode, err)

    finally:
        connection.close()
        print('Connection closed.')

except errors.Error as err:
    print('Connection refused.')
    print(err)
