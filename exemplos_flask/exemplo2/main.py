from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        rate = 5.00  # Taxa fixa de conversão
        result = amount * rate
    return render_template('converter.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
