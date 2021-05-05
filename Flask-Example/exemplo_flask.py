from flask import Flask, render_template, redirect

app = Flask(__name__)

pessoa = dict(nome="Carlos", idade=25)


@app.route("/read/")
def read():
    return render_template("index.html", pessoa=pessoa)


@app.route("/")
def index():
    return redirect("/read/")


if __name__ == "__main__":
    app.run(debug=True)
