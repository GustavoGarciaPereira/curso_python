from flask import Flask, request, redirect, render_template, url_for
import random
import string

app = Flask(__name__)
urls = {}

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    return render_template('shortener.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_short_url()
    urls[short_url] = original_url
    return render_template('shortener.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = urls.get(short_url)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
