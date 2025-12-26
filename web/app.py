from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in ["joni","atep"] and password == "admin123":
            message = 'Berhasil login'
        else:
            message = "gagal login"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)