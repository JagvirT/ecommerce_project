from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/posts')
def view_posts_api():
    post = Post
    posts_api = []