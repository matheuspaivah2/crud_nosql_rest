from flask import Flask, jsonify
from app import db


def get_one_post(app: Flask):

    @app.get("/posts/<int:id>")
    def get_one_post_from_db(id):

        data = db.posts.find_one({"_id": id})
        if data != None:
            return jsonify(data), 200
        else:
            return {'message': "Post not found"}, 404


        
        
  