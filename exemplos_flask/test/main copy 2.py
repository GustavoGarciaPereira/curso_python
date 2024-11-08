# from flask import Flask, render_template, request


# app  = Flask(__name__)


# @app.route('/<int:numero>', methods=['GET'])
# def main(numero):
#     print("ggg",numero)
#     print("\n\n\n\nrequest\n\n", type(request.form))
    
#     nome = request.form.get('informacao', '')
#     ideade = request.form.get('idade', '')
    
#     idade = request.form.get('idade',"")
#     peso = request.form.get('peso',"")
#     altura = request.form.get('altura',"")
#     genero = request.form.get('genero',"")
#     print(
#         "{} {} {} {}".format(idade,
#                     peso,
#                     altura,
#                     genero)
#     )
        
#     return render_template('formulario.html',variavel_template=nome)


# if __name__ == "__main__":
#     app.run(debug=True)
    

# from logging import Manager

from flask import Flask, render_template_string, request, session, redirect, url_for, render_template


# Create the Flask application
app = Flask(__name__, template_folder='templ')


# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = 'BAD_SECRET_KEY'


# @app.after_request
# def log_request(response):
#     print(f"Requisição para {request.path} retornou {response.status_code}")
#     if response.status_code == 404:
#         return "Rota não encontrada"
#     return response

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to the session object
        session['email'] = request.form['email_address']
        return redirect(url_for('get_email'))

    return """
        <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
        """


@app.route('/get_email')
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """)


@app.route('/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return '<h1>Session deleted!</h1>'


@app.errorhandler(404)
def pagina_nao_encontrada(e):
    print(f"ssssssssssssssss\n{e}\nsssssssssssssssss")
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()
    