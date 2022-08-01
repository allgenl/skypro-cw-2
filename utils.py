import json

DATA = "data/data.json"
BOOKMARKS = "data/bookmarks.json"
COMMENTS = "data/comments.json"

def get_posts_all():
    """Возвращает посты"""
    with open(DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_bookmarks_count():
    """Возвращается число закладок"""
    with open(BOOKMARKS, 'r', encoding='utf-8') as file:
        bookmarks_count = len(json.load(file))
    return bookmarks_count

def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    with open(DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)
    posts = [post for post in data if user_name == post["poster_name"]]
    if posts:
        return posts
    else:
        return "ValueError"


def get_comments_by_post_id(post_id):
    """Возвращается комментарии определенного поста"""
    try:
        with open(COMMENTS, 'r', encoding='utf-8') as file:
            comments_all = json.load(file)
        comments = []
        for comment in comments_all:
            if comment["post_id"] == post_id:
                comments.append(comment)
        return comments
    except ValueError:
        return "Такого поста нет"


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    with open(DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
    posts = []
    for post in data:
        if str(query).lower() in post["content"].lower():
            posts.append(post)
    return posts


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    return [post for post in posts if post["pk"] == pk]