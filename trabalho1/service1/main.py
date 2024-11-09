from flask import Flask, jsonify, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> servico</h1>"

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/form")
def form():
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, port=4000, host="0.0.0.0")