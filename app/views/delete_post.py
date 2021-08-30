from flask import Flask, jsonify
from app import db


def delete_post(app: Flask):

    @app.delete("/posts/<int:id>")
    def delete_post_from_db(id):

        try:
            data = db.posts.find_one({"_id": id})
            db.posts.delete_one(data)

            return jsonify(data), 200
        except TypeError:
            return "Fails when trying to delete", 404

