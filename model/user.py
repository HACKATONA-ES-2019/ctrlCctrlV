

class User:
    def __init__(self, username, password):
        self.user_name = username
        self.password = password

    def json(self):
        return {'username': self.user_name, 'password': self.password}

    def insert_string(self):
        return f'INSERT INTO USUARIO VALUES ("{self.username}", "{self.password}");'
