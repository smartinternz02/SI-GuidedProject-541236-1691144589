from flask import Flask,url_for,redirect

app=Flask(__name__)

@app.route("/")
def home():
    return ("Welcome All")

@app.route("/hello")
def hello():
    return  ("Hello World")

@app.route("/hi")
def hi():
    return ("Hello All Faculties, Welcome in 5 days FDP")

@app.route("/user/<enter>")
def user (enter):
    if enter== "Welcome":
       return redirect( url_for("home"))
    elif enter== "hello":
        return redirect(url_for("hello"))
    else:
        return redirect(url_for("hi"))

if __name__=="__main__":
   app.run(debug=True)