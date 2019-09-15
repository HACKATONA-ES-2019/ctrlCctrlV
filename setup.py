import json
import random
from controllers.main_handler import Handler
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
handler = Handler()

handler.add_user('admin', 'admin')
handler.add_information('Incendio', 'resources/incendio', 'resources/incendio')
handler.add_information('Deslizamento', 'resources/deslizamento', 'resources/deslizamento')
handler.add_information('Enchente', 'resources/enchente', 'resources/enchente')


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
