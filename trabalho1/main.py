from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def main():
    return "<h1> Olá Gustavo</h1>"


@app.route("/<int:numero1>/<int:numero2>/<string:sinal>")
def calculadora(numero1, numero2, sinal):
    
    print("numero1 = ", numero1)
    print("numero2 = ", numero2)
    print("sinal = ", sinal)
    if sinal == '+':
        resultado = numero1 + numero2
    else:
        resultado = numero1 - numero2
    dic = {
        "resultado": resultado,
        "numero1": numero1,
        "numero2": numero2,
        "sinal": sinal
    }
    return render_template("index.html",conta = dic)

@app.route("/forms",  methods=["GET", "POST"])
def forms():
    dic = {}
    if  request.method == "POST":

        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        status = "Cadastrado com sucesso!"
        dic = {
            "status":status,
            "nome":nome,
            "sobrenome":sobrenome
        }
        return render_template("forms.html",dic = dic)
        #return redirect(url_for("main"), nome=nome)
    return render_template("forms.html", dic=dic)


@app.route('/imc', methods=['GET', 'POST'])
def imc():
    imc = 0
    if request.method == "POST":
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        peso = int(request.form.get('peso'))
        altura = int(request.form.get('altura'))
        sexo = request.form.get('sexo')
        #IMC = Peso ÷ (Altura × Altura)
        print(f"""
            nome = {nome}
            idade = {idade}
            peso = {peso}
            altura = {altura}
            sexo = {sexo}""")
        imc = peso / (altura ** 2)

    return render_template("forms_imc.html", imc=imc)