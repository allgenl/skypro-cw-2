import json

DATA = "data/data.json"


def get_posts_all():
    """Возвращает посты"""
    with open(DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    try:
        pass
    except ValueError:
        return "Такого пользователя нет"


def get_comments_by_post_id(post_id):
    """Возвращается комментарии определенного поста"""
    try:
        pass
    except ValueError:
        return "Такого поста нет"


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    pass


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    pass