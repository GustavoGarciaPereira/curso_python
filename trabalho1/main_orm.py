from flask import Flask, jsonify, render_template, request, redirect, url_for
# from flask_swagger import swagger
# from flask_swagger_ui import get_swaggerui_blueprint
# from flask_cors import CORS  

app = Flask(__name__)
# CORS(app)
# # Swagger UI configuration
# SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
# API_URL = '/spec'         # URL for Swagger specification
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "My API"
#     }
# )
# app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# @app.route("/spec")
# def spec():
#     swag = swagger(app)
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "My API"
#     return jsonify(swag)
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

dic_senac = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"senacrs",
    "database":"saude",
    "use_pure":True
}
dic_casa = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"root_password",
    "database":"saude"
}

cnx = mysql.connector.connect(**dic_casa)


app = Flask(__name__)
from sqlalchemy import Column, Integer, String, Float, Enum, create_engine
from flask_sqlalchemy import SQLAlchemy
import enum

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root_password@127.0.0.1:3306/saude'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definindo o enum para o campo 'sexo'
class SexoEnum(enum.Enum):
    homem = "homem"
    mulher = "mulher"

# Definindo o modelo da tabela de pessoas
class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.Enum(SexoEnum), nullable=False)
    imc = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Pessoa(id={self.id}, nome='{self.nome}', idade={self.idade}, peso={self.peso}, altura={self.altura}, sexo='{self.sexo}', imc={self.imc})>"

@app.route("/")
def main():
    """
    Home route
    ---
    responses:
      200:
        description: Retorna uma mensagem de boas-vindas.
    """
    return redirect(url_for("liste_imc"))

@app.route("/<int:numero1>/<int:numero2>/<string:sinal>")
def calculadora(numero1, numero2, sinal):
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
    return render_template("index.html", conta=dic)

@app.route("/forms", methods=["GET", "POST"])
def forms():
    dic = {}
    if request.method == "POST":
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        status = "Cadastrado com sucesso!"
        dic = {
            "status": status,
            "nome": nome,
            "sobrenome": sobrenome
        }
        return render_template("forms.html", dic=dic)
    return render_template("forms.html", dic=dic)

@app.route('/imc', methods=['GET', 'POST'])
def imc():
    imc = 0
    if request.method == "POST":
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        sexo = request.form.get('sexo')
        imc = peso / (altura ** 2)
        new_pessoa = Pessoa(
            nome = nome,
            idade = idade,
            peso = peso,
            altura = altura,
            sexo = sexo,
            imc = imc
        )
        db.session.add(new_pessoa)
        db.session.commit()
        return redirect(url_for("liste_imc"))
        
    return render_template("forms_imc.html", imc=imc)

@app.route('/liste_imc')
def liste_imc():
    
    pessoas = Pessoa.query.all()
    print(pessoas)
    if len(pessoas) <= 0:
        return redirect(url_for("imc"))
    return render_template("liste_imc.html",pessoas=pessoas)


@app.route('/delete/<int:id_pessoa>')
def delete_imc(id_pessoa):
    
    sql = f"DELETE FROM pessoas where id = {id_pessoa};"
    c = cnx.cursor()
    row = c.execute(sql)
    cnx.commit()
    return redirect(url_for("liste_imc"))


if __name__ == "__main__":
    app.run(debug=True)