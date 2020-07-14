from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


app.run(host="localhost",port=80,debug=False)
