from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", message="AI 자동 일기 쓰기")

@app.route("/hello")
def hello():
    return render_template("hello.html", message="Hello, World!")

if __name__ == "__main__":
    app.run(debug=True)