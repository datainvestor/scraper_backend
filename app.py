from flask import Flask, jsonify, request
from scraper import parse_and_get_df, main_df
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/parse', methods=['POST'])
def show_episodes():
    requestJson = request.get_json(force=True)["lst"]
    print(requestJson)
    return jsonify({
        'status': 'success',
        'episodes': main_df(requestJson)
    })



if __name__ == '__main__':
    app.run(debug=True, port=5000)
