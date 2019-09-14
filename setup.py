import json
from controllers.main_handler import Handler
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
handler = Handler()


@app.route('/', methods=['GET'])
def startup():
    return render_template('startup.html')


@app.route('/cadastro', methods=['POST'])
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


@app.route('/logout', methods=['POST'])
def logout():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']

        if not handler.check_user(username):
            response['status'] = 403
            return jsonify(response)

        if handler.remove_user(username):
            response['status'] = 200
            response['result'] = True

        else:
            response['status'] = 409

    except KeyError:
        response['status'] = 400

    except json.JSONDecodeError:
        response['status'] = 406

    return jsonify(response)


@app.route('/informacoes', methods=['GET'])
def get_informations():
    response = {'status': 0, 'result': False, 'data': {}}

    try:
        data = request.get_json(force=True)

        username = data['username']
        information_title = data['title']

        if not handler.check_user(username):
            response['status'] = 403
            return jsonify(response)

        if handler.get_information(information_title):
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
    app.run()
