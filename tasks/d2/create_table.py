from mysql.connector import connect, errors, errorcode
from congif import host, user, password, db_name


create_tracked_tournaments_table_query = '''
CREATE TABLE tracked_tournaments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT PRIMARY KEY,
    league_name VARCHAR(100),
    start_date_time TIMESTAMP,
    end_date_time TIMESTAMP
)
'''

create_untracked_tournaments_table_query = '''
CREATE TABLE untracked_tournaments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT PRIMARY KEY,
    league_name VARCHAR(100),
    start_date_time TIMESTAMP,
    end_date_time TIMESTAMP
)
'''

create_match_info_table_query = '''
CREATE TABLE match_info (
    league_id INT,
    league_name VARCHAR(100),
    match_id INT PRIMARY KEY,
    radiant_team_name VARCHAR(100),
    radiant_team_id INT,
    dire_team_name VARCHAR(100),
    dire_team_id INT,
    winner VARCHAR(100),
    FOREIGN KEY (league_id) REFERENCES tracked_tournaments (league_id)
)
'''

create_picks_table_query = '''
CREATE TABLE picks (
    league_id INT,
    match_id INT,
    hero1 INT,
    hero2 INT,
    hero3 INT,
    hero4 INT,
    hero5 INT,
    hero6 INT,
    hero7 INT,
    hero8 INT,
    hero9 INT,
    hero10 INT,
    FOREIGN KEY (league_id) REFERENCES tracked_tournaments(league_id),
    FOREIGN KEY (match_id) REFERENCES match_info(match_id)
)
'''

rename_table_query = '''
ALTER TABLE tournaments
RENAME TO tracked_tournaments
'''




try:
    connection = connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print(f'Successfully connected to {db_name} database.')

    try:
        with connection.cursor() as cursor:
            # cursor.execute(create_match_info_table_query)
            cursor.execute(create_picks_table_query)
            connection.commit()
            print('Table successfully created.')
            # print('Table renamed.')
    except errors.Error as err:
        print('Unexpected error', err, errorcode)

    finally:
        connection.close()

except errors.Error as err:
    print('Connection refused.')
    print(err, errorcode)