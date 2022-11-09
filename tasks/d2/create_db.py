from mysql.connector import connect, Error
from congif import host, user, password


tournaments_db = 'CREATE DATABASE tournaments'

try:
    connection = connect(
        host=host,
        user=user,
        password=password
    )
    print('Successfully connected.')

    try:
        with connection.cursor() as cursor:
            cursor.execute(tournaments_db)
            print('Database created.')
    except:
        print('Database already exists.')

    finally:
        connection.close()

except Error:
    print('Connection refused.')
    print(Error)


