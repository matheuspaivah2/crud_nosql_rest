from flask import Flask, request

from app import db
from app.Models.post_model import Post
from .utils import check_valid_data


def register_post(app: Flask):

    @app.post("/posts")
    def register_post_in_db():

        try:
            req = request.get_json()
            if (check_valid_data(req) == False):
                return {'message': 'Request fields must contain only string'}, 400

            user_id = 0
            data_list = db.posts.find()
            data_list = list(data_list)
            
            if len(data_list) >= 1:
                user_id = data_list[-1]['_id'] + 1
            else:
                print(len(data_list))
                user_id = 1
            
            data = Post(user_id, req['title'], req['author'], req['tags'], req['content'])
            db.posts.insert_one(data.__dict__)
            
            return {'id': user_id, 'title': req['title'],'author': req['author'],'tags': req['tags'],'content': req['content']}, 201

        except KeyError:
            return {'message': 'This request is not valid'}, 400
        
  