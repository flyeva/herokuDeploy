from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_me")
def about():
    return "<h1>about me</h1>"


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()

# Model - View - Controller
