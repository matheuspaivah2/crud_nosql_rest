from flask import Flask
from flask.json import jsonify

from app import db
from app.Models.post_model import Post


def get_all_posts(app: Flask):

    @app.get("/posts")
    def get_all_posts_in_db():

        try:
            data_list = db.posts.find()
            output = [post for post in data_list]
            print(output)
            if output != []:
                return jsonify(output), 200
            else:
                return {'message': 'Empty list'}, 200


        except KeyError:
            return {'message': 'Request failed'}, 500
        
  