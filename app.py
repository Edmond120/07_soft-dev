from flask import Flask, render_template, request, session
import os

form_site = Flask(__name__)
form_site.secret_key = os.urandom(16)

@form_site.route("/", methods=['POST', 'GET'])
def root():
    print request.form
    return render_template('temp.html')

@form_site.route("/welcome", methods=['POST', 'GET'])
def welcome():
    if(len(session) > 0):
        username = session["username"]
        password = session["password"]
    else:
        username = request.form["username"]
        password = request.form["password"]
    if(username != "bob" and password != "123"):
        return render_template('temp.html',status="wrong username and password")
    elif (username != "bob"):
        return render_template('temp.html',status="wrong username")
    elif (password != "123"):
        return render_template('temp.html',status="wrong password")
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]
    return render_template('access.html', name=request.form["username"])

if __name__ == '__main__':
    form_site.debug = True
    form_site.run()
    
