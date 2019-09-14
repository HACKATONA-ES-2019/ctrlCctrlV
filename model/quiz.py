

class Quiz:
    def __init__(self, quiz_title):
        self.quiz_title = quiz_title

    def json(self):
        return self.quiz_title

    def insert_into(self):
        return f'INSERT INTO QUIZ VALUES ("{self.quiz_title}");'
