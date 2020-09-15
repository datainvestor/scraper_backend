from flask import Flask, jsonify, request
from scraper import parse_and_get_df, main_df
from flask_cors import CORS
from flask_restful import Api

from db import db
from resources.shows import Show, ShowsList

# instantiate the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'aagg'
CORS(app, resources={r'/*': {'origins': '*'}})
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Show, '/show/<string:imdb_key>')
api.add_resource(ShowsList, '/shows')

# @app.route('/parse', methods=['POST'])
# def show_episodes():
#     requestJson = request.get_json(force=True)["lst"]
#     print(requestJson)
#     return {
#         'status': 'success',
#         'episodes': main_df(requestJson)
#     }


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
