from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route("/")
def Hello():
    return "<h1>HELLO FLASK!</h1>"

@app.route("/about")
def about():
    name = "Harry"
    return render_template('index.html', name=name)

@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=0, debug=True)


