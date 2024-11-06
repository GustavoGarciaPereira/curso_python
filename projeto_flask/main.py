from flask import Flask, render_template


app  = Flask(__name__)


@app.route("/")
def gustavo():
    lista = [1,2,3,4,5]
    return render_template("index.html", nome=lista)
    

