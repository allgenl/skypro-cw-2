import api as api
import werkzeug
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import NotFound, InternalServerError
from utils import get_posts_all, get_bookmarks_count, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False


    @app.route('/',  methods=["GET"])
    def index():
        """Эта вьюшка показывает ленту"""
        posts = get_posts_all()
        bookmarks_count = get_bookmarks_count()
        return render_template("index.html", posts=posts, bookmarks_count=bookmarks_count)


    @app.route('/posts/<int:postid>', methods=["GET"])
    def post(postid):
        """Эта вьюшка показывает пост по его pk"""
        post = get_post_by_pk(postid)
        comments = get_comments_by_post_id(postid)
        comments_count = len(comments)
        return render_template("post.html", comments=comments, post=post, comments_count=comments_count)

    @app.route('/search', methods=["GET"])
    def search():
        search_word = request.args.get('s')
        posts = search_for_posts(search_word)
        posts_count = len(posts)
        return render_template("search.html", posts=posts, posts_count=posts_count)


    @app.route('/users/<username>', methods=["GET"])
    def user(username):
        posts = get_posts_by_user(username)
        if posts == "ValueError":
            return "<h1>Такого пользователя не существует</h1>"
        else:
            return render_template("user-feed.html", posts=posts)


    @app.route('/api/posts', methods=["GET"])
    def api_posts():
        posts = get_posts_all()
        return jsonify(posts)


    @app.route('/api/posts/<int:post_id>', methods=["GET"])
    def api_posts_by_id(post_id):
        post = get_post_by_pk(post_id)
        return jsonify(post[0])


    @app.errorhandler(werkzeug.exceptions.NotFound)
    def handler(e):
        return "<h1>Страница не найдена</h1>", 404

    @app.errorhandler(werkzeug.exceptions.InternalServerError)
    def handler(e):
        return "<h1>Ошибка на стороне сервера</h1>", 505


    app.run(debug=True)

