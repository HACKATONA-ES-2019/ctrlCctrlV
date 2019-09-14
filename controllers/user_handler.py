from model.user import User


class UserManager:
    def __init__(self):
        self.session_user = {}

    def add_user(self, session_id, username, password):
        if session_id in self.session_user:
            return False

        self.session_user[session_id] = User(username, password)
        return True

    def remove_user(self, session_id):
        if session_id not in self.session_user:
            return False

        del self.session_user[session_id]
        return True

    def get_user(self, session_id):
        return self.session_user[session_id].json()

    def check_user(self, session_id):
        return session_id in self.session_user

