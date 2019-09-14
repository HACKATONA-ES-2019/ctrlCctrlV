from model.quiz import Quiz
from model.question import Question
from model.answer import Answer


class QuizManager:
    def __init__(self):
        self.quizzes = {}

    def add_quiz(self, quiz_title, question_text, answers_texts, answer_number):
        if quiz_title in self.quizzes:
            return False

        quiz = Quiz(quiz_title)
        question = Question(question_text, answer_number)
        answers = []
        for text in answers_texts:
            answers.append(Answer(text))

        self.quizzes[quiz_title] = {'quiz': quiz, 'question': question, 'answers': answers}
        return True

    def remove_quiz(self, quiz_title):
        if quiz_title not in self.quizzes:
            return False

        del self.quizzes[quiz_title]
        return True

    def check_quiz(self, quiz_title):
        return quiz_title in self.quizzes

    def get_quiz(self, quiz_title):
        obj = self.quizzes[quiz_title]

        json_quiz = obj['quizz'].json()
        json_question = obj['question'].json()
        json_answers = [answer.json() for answer in obj['answers']]

