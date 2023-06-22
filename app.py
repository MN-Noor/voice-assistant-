import os
import uuid
from flask import Flask, flash, request, redirect, render_template ,url_for
import gsp,codex

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'aymen678564564'  # Set a secret key for flash messages

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/save-record', methods=['POST', 'GET'])
def save_record():
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    transcript=gsp.transcription(file_name)
    prompt ="Postgres SQL tables, with their properties:"+transcript
    Query=generate_sql_query(prompt)

    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    flash('File successfully uploaded')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=86)
