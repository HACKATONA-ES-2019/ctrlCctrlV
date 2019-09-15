import json
import random
from controllers.main_handler import Handler
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
handler = Handler()

# a = handler.get_quizzes()
aux = handler.get_quiz('Quiz incendio')

# handler.add_user('admin', 'admin')
# handler.add_information('Incendio', 'resources/incendio', 'resources/incendio')
# handler.add_information('Deslizamento', 'resources/deslizamento', 'resources/deslizamento')
# handler.add_information('Enchente', 'resources/enchente', 'resources/enchente')
# handler.add_quiz('Quiz incendio')
#
# from model.answer import Answer
#
# answers1 = [
#     Answer('Ficar no local e esperar socorro', 0),
#     Answer('Tentar apagar o fogo por contra própria', 0),
#     Answer('Ligar o chuveiro e ficar de baixo dele', 0),
#     Answer('Procurar uma saída mantendo-se abaixado sob a fumaça com um lenço sobre as vias respiratórias', 1)
# ]
# handler.add_question('Quiz incendio', 'Em caso de incêndio em um local fechado e com fumaça, qual a melhor decisão para se tomar', answers1)
#
#
# answers2 = [
#     Answer('Acalmar a criança e sair pela porta que não está pegando fogo', 1),
#     Answer('Chamar socorro se, e somente se, o fogo estiver fora de controle', 0),
#     Answer('Tranquilizar a criança e deixá-la no banheiro', 0),
#     Answer('Deixar a criança sozinha e procurar socorro', 0)
# ]
# handler.add_question('Quiz incendio', 'Se você está supervisionando uma criança e há princípio de fogo, você faz', answers2)
#
# answers3 = [
#     Answer('Manter objetos inflamáveis próximo ao fogo', 0),
#     Answer('Mato seco no quintal', 0),
#     Answer('Manter os extintores de incêndios em locais estratégicos', 1),
#     Answer('Todas as alternativas', 0)
# ]
#
# handler.add_question('Quiz incendio', 'Para prevenir os incêndios, é necessário, no mínimo', answers3)


@app.route('/', methods=['GET'])
def get_login_html():
    return render_template('login.html')


@app.route('/cadastro', methods=['GET'])
def get_cadastro_html():
    return render_template('register.html')


@app.route('/home', methods=['GET'])
def get_home_html():
    return render_template('home.html')


@app.route('/tutoriais')
def get_tutoriais_html():
    tutoriais = handler.get_informations()
    return render_template('tutorial.html', tutoriais=tutoriais)


@app.route('/tutorial/<tutorial_name>')
def get_tutorial_html(tutorial_name):
    tutorial_obj = handler.get_information(tutorial_name).json()
    tutorial_name = tutorial_obj['title']
    tutorial_text = tutorial_obj['text']
    return render_template('general_page.html', tutorial_name=tutorial_name, tutorial_text=tutorial_text)


@app.route('/contato')
def get_contato_html():
    return render_template('contato.html')


@app.route('/quiz', methods=['GET'])
def get_quizzes_html():
    quizzes = handler.get_quizzes()
    return render_template('quizzes.html', quizzes=quizzes)


@app.route('/quiz/<quiz_title>', methods=['GET'])
def get_quiz_html(quiz_title):
    quiz_title = str(quiz_title).replace('_', ' ')
    questions = handler.get_quiz(quiz_title)
    return render_template('quiz.html', quiz_title=quiz_title, questions=questions[quiz_title])


@app.route('/register', methods=['POST'])
def register():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']
        password = data['password']

        if handler.add_user(username, password):
            response['status'] = 200
            response['result'] = True

        else:
            response['status'] = 409

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/login', methods=['POST'])
def login():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']
        password = data['password']

        if handler.get_user_by_username(username, password):
            response['status'] = 200
            response['result'] = True

        else:
            response['status'] = 409

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.config['SESSION_REFRESH_EACH_REQUEST'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['SECRET_KEY'] = float(random.randrange(100, 150000))/100
    app.run()
