from flask import flask, render_template, request
import ibm_db

app=flask (__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud",PORT=32286;USERID=mmz19732;PASSWORD=G6obu8J6BTVJxqbl;SECURITY=ssl;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt;",'','')
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

  
    @app.route("/contact")
    def contact():
       return render_template("contact.html")

    @app.route("/login")
    def login():
      if request.method== "POST":
          uname = request.form['username']
          pword = request.form['password']
          print(username,pword_)
    return render_template("login.html") 
        

    if __name__=="__main__":
        app.run(debug= True)
        