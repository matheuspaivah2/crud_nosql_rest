from flask import Flask

def init_app(app: Flask):
  
    from app.views.register_post import register_post
    register_post(app)

    from app.views.get_all_posts import get_all_posts
    get_all_posts(app)

    from app.views.get_one_post import get_one_post
    get_one_post(app)

    from app.views.delete_post import delete_post
    delete_post(app)

    from app.views.update_post import update_post
    update_post(app)

    return app