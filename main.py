import requests
from flask import Flask, render_template


app = Flask(__name__)
blog_url = "https://api.npoint.io/4af156202f984d3464c3"


@app.route("/")
def home():
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:post_id>")
def post(post_id):
    response = requests.get(blog_url)
    all_posts = response.json()

    for post in all_posts:
        if post["id"] == post_id:
            title = post["title"]
            body = post["body"]
    return render_template("post.html", title=title, body=body)


if __name__ == "__main__":
    app.run(debug=True)
