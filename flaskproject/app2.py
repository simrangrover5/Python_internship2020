from flask import Flask,render_template

app = Flask(__name__)

#templates --> html pages
#static --> css, images, bs etc

@app.route("/")
def index():
    return render_template("abc.html")  #templates/abc.html
    #templates --> html_files --> abc.html
    #render_template(html_files/abc.html)
    #render_template will go itself to the template folder and find abc.html and return it to browser


#.xyz --> python --> jinja
#jinja --> templating engine of python
#use python in html file using jinja
#jinja --> key value pair
#client                    server
# {{name}}                name = simran
# if else --> 
"""
    {% if condition %}     {% if condition %}    {% if condition %}
        <h1>                   <h1>                <h1>
        <p>                 {% else %}           {% elif condition %}
    {% endif %}                 <p>                 <p>
                            {% endif %}                 {% if condition %}
                                                            <h1>
                                                        {% endif %} 
                                                {% else %}
                                                    <li>
                                                  {% endif %}   
"""
#for loop --> 
""" {% for i in range(10) %}
        <h1>Hello </h1>
    {% endfor %}
"""

@app.route("/home/<name>/<interest>/")
def home(name,interest):
    return render_template("abc.html",n = name,inter = interest)

@app.route("/home/<name1>/<name2>/<name3>/")
def get_name(name1,name2,name3):
    d = {
        "Father" : name1,
        "Mother" : name2,
        "Child" : name3
    }
    return render_template("abc.html",data=d)

app.run(host="localhost",port=80,debug=True)