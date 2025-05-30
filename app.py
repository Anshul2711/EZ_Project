"""
File Sharing System
Developed by: Aviral Bhadouria
"""

from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home Route
@app.route('/')
def index():
    return render_template('upload.html')

# Upload Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('list_files'))

# List Files for Download
@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('download.html', files=files)

# Download Route
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
