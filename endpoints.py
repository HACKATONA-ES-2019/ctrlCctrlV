import json
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
users_sessions = {}


@app.route('/', methods=['GET'])
def startup():
    return render_template('startup.html')


@app.route('/login', methods=['POST'])
def login():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']
        password = data['password']

        users_sessions[session.sid] = username

        response['status'] = 200
        response['result'] = True

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/logout', methods=['POST'])
def logout():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']

        if username == users_sessions[session.sid]:
            del users_sessions[session.sid]

        response['status'] = 200
        response['result'] = True

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/informacoes', methods=['GET'])
def get_informacoes_desastre():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        tipo_desastre = data['desastre']

        response['status'] = 200
        response['result'] = True

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/quiz', methods=['GET'])
def get_quiz_usuario():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        response['status'] = 200
        response['result'] = True

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)

