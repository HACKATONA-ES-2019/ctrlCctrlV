

class Question:
    def __init__(self, question_title, answers):
        self.question_title = question_title
        self.answers = answers

    def get_answer(self):
        for answer in self.answers:
            if answer.right:
                return answer

        return None
