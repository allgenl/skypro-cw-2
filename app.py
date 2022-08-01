from flask import Flask, render_template, request
from utils import get_posts_all
import json

if __name__ == '__main__':
    app = Flask(__name__)


    @app.route('/')
    def index():
        posts = get_posts_all()
        return render_template("index.html", posts=posts)


    app.run(debug=True)

