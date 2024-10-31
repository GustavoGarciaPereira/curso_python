from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=8, use_digits=True, use_upper=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_upper:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_digits = 'digits' in request.form
        use_upper = 'upper' in request.form
        use_symbols = 'symbols' in request.form
        password = generate_password(length, use_digits, use_upper, use_symbols)
    return render_template('password_generator.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
