from __future__ import annotations

from flask import Blueprint, render_template
from werkzeug.exceptions import abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO
from config import DATA_PATH_POSTS, DATA_PATH_BOOKMARKS, DATA_PATH_COMMENTS

# Создаем блупринт
posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")

# Создаем объекты доступа к данным
post_dao = PostDAO(DATA_PATH_POSTS)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)


@posts_blueprint.route("/")
def page_posts_index():
    """ Страничка всех постов """

    all_posts = post_dao.get_all()

    return render_template("posts_index.html", posts=all_posts)


@posts_blueprint.route("/posts/<int:pk>/")
def page_post_by_pk(pk: int):
    """ Страничка одного поста """

    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comment_dao.get_comments_by_post_pk(pk)
    comments_count: int = len(comments)

    if post is None:
        abort(404)

    return render_template("posts_single.html",
                           post=post,
                           comments=comments,
                           comments_count=comments_count
                           )


@posts_blueprint.route("/users/<string:user_name>")
def page_posts_by_users(user_name: str):
    posts = post_dao.get_by_poster(user_name)

    return render_template("posts_user-feed.html", posts=posts)

