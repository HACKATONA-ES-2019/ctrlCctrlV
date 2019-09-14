from controllers.user_handler import UserManager


class Handler:
    def __init__(self):
        self.user_manager = UserManager()

    def add_user(self, session_id, username, password):
        return self.user_manager.add_user(session_id, username, password)

    def remove_user(self, session_id):
        return self.user_manager.remove_user(session_id)

    def check_user(self, session_id):
        return self.user_manager.check_user(session_id)

    def get_user(self, session_id):
        return self.user_manager.get_user(session_id)
