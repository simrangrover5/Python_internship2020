from flask import Flask,render_template,request,make_response,session
from flask import redirect,url_for
import pymysql as sql
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests

app = Flask(__name__)
app.secret_key = "hfiejjfoijepijepijoiejowlkmsknjdnoejpipwjojoiji"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    if session.get("islogin"):
    #if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("login.html")

@app.route("/signup/")
def signup():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("signup.html")

@app.route("/afterlogin/",methods=['POST','GET'])  #methods --> http method
def afterlogin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            db = sql.connect(host="localhost",port=3306,database="internship_batch",user="root",password="")
            cursor = db.cursor()
            cmd = f"select * from users where email='{email}'"
            cursor.execute(cmd)
            data = cursor.fetchone() #return tuple
            #(email,password,gender)
            if data:
                #print(data)
                #means user exists allow login
                if data[1] == password:
                    #resp = make_response(render_template("afterlogin.html"))
                    #resp.set_cookie("email",email)
                    #resp.set_cookie("islogin","true")
                    #return resp
                    session['email'] = email
                    session['islogin'] = "true"
                    return render_template("afterlogin.html")
                    #return render_template("abc.html")
                else:
                    error = "Password does not matched!!!!"
                    return render_template("login.html",error=error)
            else:
                #means user does not exists and not allow user to login
                error = "Invalid user"
                return render_template("login.html",error=error)
        except Exception as e:
            return f"{e}"
    else:
        return render_template("login.html")

@app.route("/aftersignup/",methods=["GET","POST"])
def aftersignup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("passwd")
        gender = request.form.get("gender")
        try:
            db = sql.connect(host="localhost",port=3306,user="root",password="",database="internship_batch")
            cursor = db.cursor()
            cmd = f"select * from users where email='{email}'"
            cursor.execute(cmd)
            data = cursor.fetchone() #if there is empty set then fetchone will return None and condition will get false
            if data:  #if there exists one tuple then it will return true else False
                error = "Email Already exists"
                return render_template("signup.html",error=error)
            else:
                s = 0
                l = 0
                u = 0
                n = 0
                if len(password) >= 8:
                    for i in password:
                        if i.isupper():
                            u += 1
                        if i.islower():
                            l += 1
                        if i in ["@","#","*"," ","%","$","^","&"]:
                            s += 1
                        if i.isnumeric():
                            n += 1
                    else:
                        if s>=1 and l>=1 and u>=1 and n>=1:
                            from_email = "simrangrover5@gmail.com"
                            to_email = email
                            p = os.environ.get("EMAIL_HOST_PASSWORD")
                            message = MIMEMultipart("alternative")
                            message["Subject"] = "Mail for your account activation"
                            message["To"] = to_email
                            message["From"] = from_email
                            html = """
                                <h1 style='color:red'>Your activation link is as follows</h1>
                                <a href="localhost/activate/">CLient on this link<a>
                                """
                            msg = MIMEText(html,"html")
                            message.attach(msg)
                            context = ssl.create_default_context()
                            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
                                server.login(from_email,p)
                                server.sendmail(from_email,to_email,message.as_string())
                                session['email'] = email
                                session['password'] = password
                                session['gender'] = gender
                            return render_template("index.html")
                        else:
                            error = "Password does not match the conditions"
                            return render_template("signup.html",error=error)
                else:
                    error = "Password must be of 8 characters long"
                    return render_template("signup.html",error=error)
        except Exception as e:
            return f"{e}"
    else:
        return render_template("signup.html")
    
@app.route("/logout/")
def logout():
    #resp = make_response(render_template("login.html"))
    #resp.delete_cookie("email")
    #resp.delete_cookie("islogin")
    del session['email']
    del session['islogin']
    return redirect(url_for("login"))  #redirect to the url of login function --> /login/

@app.route("/activate/")
def account_activate():
    try:
        email = session.get("email")
        password = session.get("password")
        gender = session.get("gender")
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="internship_batch")
        cursor = db.cursor()
        cmd = f"insert into users values('{email}','{password}','{gender}')"
        cursor.execute(cmd)
        db.commit()
        del session['email']
        del session['password']
        del session['gender']
        error = "Login to continue....."
        return render_template("login.html",error=error)
    except Exception as e:
        return f"{e}"

@app.route("/todayweath/",methods=['GET','POST'])
def weath_html():
    if request.method == "GET":
        return render_template("weather.html")
    elif request.method == "POST":
        city = request.form.get("city")
        api_key = "e9034b1eee3034977886c9f275b27127"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
            desc = data['weather'][0]['description']
            temp = round(data['main']['temp'] - 273.15,2)
            humidity = data['main']['humidity']
            min_temp = data['main']['temp_min'] - 273.15
            max_temp = data['main']['temp_max'] - 273.15
            country = data['sys']['country']
            icon = data['weather'][0]['icon']
            weather = {
                "Description" : desc,
                "Temperature" : temp,
                "Humidity" : humidity,
                "Min_temp" : min_temp,
                "Max_temp" : max_temp,
                "Country" : country,
            }
            return render_template("weather.html",data=weather,icon=icon)
        

#return signup form 
app.run(host="localhost",port=80,debug=True)