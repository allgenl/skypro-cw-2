from flask import Flask, render_template, request
from utils import get_posts_all, get_bookmarks_count, get_comments_by_post_id, get_post_by_pk
import json

if __name__ == '__main__':
    app = Flask(__name__)


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

    app.run(debug=True)

