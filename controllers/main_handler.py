from controllers.user_handler import UserManager
from controllers.information_handler import InformationManager
from controllers.db_handler import DBHandler


class Handler:
    def __init__(self):
        self.user_manager = UserManager()
        self.information_manager = InformationManager()
        self.db_handler = DBHandler()

    def add_user(self, username, password):
        if self.user_manager.add_user(username, password):
            user_query = self.user_manager.get_user(username).insert_string()
            if self.db_handler.insert(user_query):
                return True

        return False

    def remove_user(self, session_id):
        return self.user_manager.remove_user(session_id)

    def check_user(self, session_id):
        return self.user_manager.check_user(session_id)

    def get_user_by_session(self, session_id):
        return self.user_manager.get_user(session_id)

    def get_user_by_username(self, username, password):
        user = self.db_handler.get_user(username)
        if user and user[1] == password:
            self.user_manager.add_user(username, password)
            return True

        return False

    def add_information(self, information_title, information_text_path, information_images_path):
        if self.information_manager.add_information(information_title, information_text_path, information_images_path):
            information_query = self.information_manager.get_information(information_title).insert_string()
            if self.db_handler.insert(information_query):
                return True

        return False

    def get_information(self, information_title):
        info = self.db_handler.get_information(information_title)
        if info:
            if not self.information_manager.check_information(information_title):
                self.information_manager.add_information(*info)

            return self.information_manager.get_information(information_title)

        return None
