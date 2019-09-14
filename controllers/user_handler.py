from model.user import User


class UserManager:
    def __init__(self):
        self.user = {}

    def add_user(self, username, password):
        if username in self.user:
            return False

        self.user[username] = User(username, password)
        return True

    def remove_user(self, username):
        if username not in self.user:
            return False

        del self.user[username]
        return True

    def check_user(self, username):
        return username in self.user

    def get_user(self, username):
        return self.user[username]

