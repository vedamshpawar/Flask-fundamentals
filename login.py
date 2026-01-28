from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        uname = request.form.get ('uname')
        password = request.form.get ('pass')
        if uname == "rajaka" and password == "1234":
            return "Welcome, your Login succesfull"
        else:
            return "Invalid name and password retry"
    else:
        return render_template("login.html")







if __name__ == "__main__":
    app.run(debug=True)