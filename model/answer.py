

class Answer:
    def __init__(self, answer_text):
        self.answer_text = answer_text

    def json(self):
        return self.answer_text

    def insert_into(self, question_id, answer_id):
        return f'INSERT INTO RESPOSTA VALUES ("{question_id}", "{answer_id}", "{self.answer_text}");'
