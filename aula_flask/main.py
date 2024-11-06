from flask import Flask, render_template


app = Flask("app")


@app.route("/meu_nome")
def main():
    return render_template("index.html")