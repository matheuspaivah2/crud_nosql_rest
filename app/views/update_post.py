from flask import Flask, jsonify, request
from app import db
from datetime import datetime
from .utils import check_valid_data


def update_post(app: Flask):

    @app.patch("/posts/<int:id>")
    def update_post_from_db(id):

        try:
            req = request.get_json()

            if check_valid_data(req) == False:
                return {'message': 'Request fields must contain only string'}, 400
            req['updated_at'] = datetime.utcnow()
            update = {"$set": req}
            data = db.posts.find_one({"_id": id})
            db.posts.update_one(data, update)
            
            output = db.posts.find_one({"_id": id})
            return jsonify(output), 200
        except TypeError:
            return {'message': "Post not found"}, 404
