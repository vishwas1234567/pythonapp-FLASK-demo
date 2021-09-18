from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")  
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

@app.route('/submit',methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return f"Login successfully by post method, Hello {user}"
    else:
        user = request.args.get('nm')
        return f"Login successfully by get method, Hello {user}"


if __name__ == "__main__":
    app.run()