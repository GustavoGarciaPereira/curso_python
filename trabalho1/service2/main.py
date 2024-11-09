from flask import Flask, jsonify, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> servico 2</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=4001)