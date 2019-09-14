import json
from controllers.main_handler import Handler
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
handler = Handler()


@app.route('www.google.com/', methods=['GET'])
def startup():
    return render_template('startup.html')


@app.route('/login', methods=['POST'])
def login():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']
        password = data['password']

        if handler.add_user(session.sid, username, password):
            response['status'] = 200
            response['result'] = True

        else:
            response['status'] = 409

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/logout', methods=['POST'])
def logout():
    response = {'status': 0, 'result': False, 'data': {}}

    if not handler.check_user(session.sid):
        response['status'] = 403
        return jsonify(response)

    try:
        data = request.get_json(force=True)

        handler.remove_user(session.sid)

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

    if not handler.check_user(session.sid):
        response['status'] = 403
        return jsonify(response)

    try:
        data = request.get_json(force=True)

        username = handler.get_user(session.sid)
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

    if not handler.check_user(session.sid):
        response['status'] = 403
        return jsonify(response)

    try:
        data = request.get_json(force=True)

        username = handler.get_user(session.sid)
        quiz_name = data['quiz']

        response['status'] = 200
        response['result'] = True

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)

