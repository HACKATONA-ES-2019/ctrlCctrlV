import sqlite3


class DBHandler:
    def __init__(self):
        database = sqlite3.connect('database/local_db.db')
        try:
            database.executescript(open('database/structure.sql', 'r', encoding='utf-8').read())
            database.commit()
        except sqlite3.OperationalError as sql_error:
            if str(sql_error).endswith('already exists'):
                pass
            else:
                raise sql_error

    def insert(self, query):
        try:
            with sqlite3.connect('database/local_db.db') as con:
                cursor = con.cursor()
                cursor.execute(query)
        except sqlite3.IntegrityError:
            return True

        return True

    def get_user(self, username):
        query = f'SELECT * FROM APP_USER WHERE USERNAME = "{username}";'

        with sqlite3.connect('database/local_db.db') as con:
            recovered = con.cursor().execute(query).fetchall()
            if not recovered:
                return ()

            return recovered[0]

    def get_information(self, information_title):
        query = f'SELECT * FROM INFORMATION WHERE TITLE = "{information_title}";'

        with sqlite3.connect('database/local_db.db') as con:
            recovered = con.cursor().execute(query).fetchall()
            if not recovered:
                return ()

            return recovered[0]

    def get_informations(self):
        query = f'SELECT * FROM INFORMATION'

        with sqlite3.connect('database/local_db.db') as con:
            recovered = con.cursor().execute(query).fetchall()
            return recovered
