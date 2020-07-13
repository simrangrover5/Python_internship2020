from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'>hi world</h1>"

@app.route("/home/")
def home():
    return "hello to my home"

@app.route("/hello/")
    return "Python is supernice"

app.run(debug=True)
