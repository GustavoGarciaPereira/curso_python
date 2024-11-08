from flask import render_template

def main(num1, num2, sinal):
    if sinal == '+':
        return f"<h1>{num1} + {num2} = {num1 + num2}</h1>"
    return "Não encontrado", 404

def home():
    return ">>"#render_template('index.html')

def cadastro():
    return render_template('cadastro.html')

def listagem():
    return render_template('listagem.html')
