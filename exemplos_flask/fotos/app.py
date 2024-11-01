import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16 MB para o upload

# Lista para armazenar o nome e caminho da imagem
photos = []

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' not in request.files:
        return redirect(request.url)
    
    photo = request.files['photo']
    name = request.form['name']

    if photo.filename == '':
        return redirect(request.url)

    if photo:
        filename = secure_filename(photo.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(filepath)
        
        # Adiciona o nome e caminho da foto à lista
        photos.append({'name': name, 'filepath': filepath})
        return redirect(url_for('gallery'))

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
