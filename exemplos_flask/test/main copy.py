from flask import Flask, render_template, request


app  = Flask(__name__)


@app.route('/<int:numero>', methods=['GET'])
def main(numero):
    print("ggg",numero)
    print("\n\n\n\nrequest\n\n", type(request.form))
    
    nome = request.form.get('informacao', '')
    ideade = request.form.get('idade', '')
    
    idade = request.form.get('idade',"")
    peso = request.form.get('peso',"")
    altura = request.form.get('altura',"")
    genero = request.form.get('genero',"")
    print(
        "{} {} {} {}".format(idade,
                    peso,
                    altura,
                    genero)
    )
        
    return render_template('formulario.html',variavel_template=nome)


if __name__ == "__main__":
    app.run(debug=True)
    
    
    

