from flask import Flask, request, render_template
import json


app = Flask(__name__)

game_state = {}

@app.route('/get_data', methods=['GET'])
def get_data():
    return game_state, 200


@app.route('/gsi', methods=['POST'])
def gsi():
    global game_state
    game_state = request.json
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
