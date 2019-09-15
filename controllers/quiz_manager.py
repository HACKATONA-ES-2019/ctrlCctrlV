from model.quiz import Quiz


class QuizManager:
    def __init__(self):
        self.quiz_list = {}

    def add_quiz(self, quiz_title):
        self.quiz_list[quiz_title] = Quiz(quiz_title)

    def add_question(self, quiz_title, question_title, answers_list):
        self.quiz_list[quiz_title].add_question(question_title, answers_list)
