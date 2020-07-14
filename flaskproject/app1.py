from flask import Flask

app = Flask(__name__) #__name__ --> flaskproject
#Flask --> class (present working space)
#app --> object of Flask class
#__name__ --> __main__??
#module --> file with py extension
#www.google.com/internships/
 #google.com --> domain --> / 
 #/internships/ --> path
#development environment ---> domain --> localhost --> 127.0.0.1

@app.route("/")  #/ --> example.com  
def index():
    return "Hello world"

@app.route("/home/")
def home():
    return "<h1 style='color:red'>Welcome to my home of python</h1>"

@app.route("/home/myhome/")
def myhome():
    return """<h1>Welcome to my world of python</h1>
            <p style='color:green'>Stay away from people and be safe</p>
            """
#the thing return by the function is shown in the browser
#variable path --> <var_name> type of variable by default is string
#<int:num1> , <int:num2> , <float:f1> 
@app.route("/home/<name>/")
def welcome(name):
    return f"<h1 style='color:coral;font-style:italic'>Welcoming {name} to my home of flask</h1>"

@app.route("/home/<name>/<int:age>/")
def checkvote(name,age):
    if age>=18:
        return f"<h1 style='color:coral;font-style:italic'> {name} can vote</h1>"
    else:
        return f"<h1 style='color:coral;font-style:italic'>{name} cannot vote</h1>"

app.run(host="localhost",port=800,debug=True)
#host --> domain
#port --> gateway
#debug = True --> show error on webpage (browser)
#debug = False --> whenever your are deploying your project 
#path --> localhost/simran/50/60/70/80/
#calculate the percentage and then return the percentage and grade
# per<=40 --> F
# 40<per<=50 --> E
# 50<per<=55 --> D
# 55<per<=60 --> C
# 60 - 70 --> B
# 70 - 80 --> B+
# 80 - 90 --> A
# 90 - 100 --> A+
#return simran has 65 and grade B
