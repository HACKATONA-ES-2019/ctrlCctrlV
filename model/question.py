

class Question:
    def __init__(self, question_text, correct_answer_number):
        self.question_text = question_text
        self.correct_answer_number = correct_answer_number

    def json(self):
        return self.question_text

    def insert_into(self, quiz_title):
        return f'INSERT INTO QUESTAO VALUES ("{quiz_title}", "{self.question_text}", "{self.correct_answer_number}");'
