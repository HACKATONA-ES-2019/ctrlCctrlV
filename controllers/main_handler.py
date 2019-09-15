from controllers.user_handler import UserManager
from controllers.information_handler import InformationManager
from controllers.db_handler import DBHandler
from controllers.quiz_manager import QuizManager


class Handler:
    def __init__(self):
        self.user_manager = UserManager()
        self.information_manager = InformationManager()
        self.db_handler = DBHandler()
        self.quiz_manager = QuizManager()

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

    def get_informations(self):
        infos = self.db_handler.get_informations()
        tutoriais_names = []
        for info in infos:
            tutoriais_names.append(info[0])

        return tutoriais_names

    def add_quiz(self, quiz_title):
        self.quiz_manager.add_quiz(quiz_title)

    def add_question(self, quiz_title, question_title, answers):
        self.quiz_manager.add_question(quiz_title, question_title, answers)

        insert_quiz_query = f'INSERT INTO QUIZ VALUES ("{quiz_title}");'
        insert_question_query = f'INSERT INTO QUESTION VALUES ("{question_title}", "{quiz_title}");'
        insert_answers_query = []
        for ans in answers:
            insert_answers_query.append(f'INSERT INTO ANSWER VALUES ("{ans.text}", {1 if ans.right else 0}, "{question_title}");')

        self.db_handler.insert(insert_quiz_query)
        self.db_handler.insert(insert_question_query)
        for answer_query in insert_answers_query:
            self.db_handler.insert(answer_query)

    def get_quizzes(self):
        quizzes = self.db_handler.get_quizzes()
        quizzes_names = set()
        for quiz in set(quizzes):
            quizzes_names.add(quiz[0])

        return quizzes_names

    def get_quiz(self, quiz_title):
        question_quiz, questions_obj = self.db_handler.get_quiz(quiz_title)

        page_object = {}
        for question, quiz in question_quiz:
            if quiz not in page_object:
                page_object[quiz] = {}

            page_object[quiz][question] = [(answer, correct) for answer, correct, _ in questions_obj[question]]

        return page_object
