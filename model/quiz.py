from model.question import Question


class Quiz:
    def __init__(self, quiz_title):
        self.quiz_title = quiz_title
        self.questions = []

    def add_question(self, question_title, answers):
        self.questions.append(Question(question_title, answers))

    def get_answer(self, question_text):
        for quest in self.questions:
            if quest.title == question_text:
                return quest.get_answer()

        return None
