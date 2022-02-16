#!/usr/bin/env python3

"""Blog project
Using flask(jinja) and API requests
"""
__author__ = "Aleksandr Verevkin"
import requests
from flask import Flask, render_template
from post import Post
app = Flask(__name__)

BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"
blog = requests.get(BLOG_API).json()
posts = []
for post in blog:
    posts.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))


@app.route('/blog')
def home():
    return render_template("index.html", blog=blog)


@app.route('/post/<int:id_>')
def get_post(id_):
    for article in posts:
        if article.id_ == id_:
            opened_post = article
            break
    else:
        opened_post = posts[0]
    return render_template("post.html", post=opened_post)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
