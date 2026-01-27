from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5) 


db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Interger, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email
    


@app.route("/")
def home():
    return render_template("base.html", name="Admin")


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f'<h1>{user}</h1>'
    else:
        flash("your not logged in!")
        return redirect(url_for("login"))
    
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)