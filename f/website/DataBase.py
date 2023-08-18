import sqlite3
from os import path

database_file = 'mydatabase.db'

if not path.exists(database_file):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                first_name TEXT UNIQUE NOT NULL,
                last_name TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                number INTEGER UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        '''

        cursor.execute(create_table_query)
        conn.commit()
        print('Created Database and Table')

    except sqlite3.Error as e:
        print('An error occurred:', e)

    finally:
        if conn:
            conn.close()

else:
    print('Database and Table already exist')
