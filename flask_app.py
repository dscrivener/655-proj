import os
from flask import Flask, request
import requests

UPLOAD_FOLDER = './upload'
HOST = 'localhost'
PORT = '8000'
WORKER_IP = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'ERROR: No file submitted.'
        file1 = request.files['file1']
        #path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        #file1.save(path)

        # make sure the file has the right MIME type
        # and is not too large
        if not (file1.content_type == 'image/jpeg' or file1.content_type == 'image/png'):
            return 'ERROR: File must be in .png or .jpg format.'
        elif (file1.content_length > 10000000):
            return 'ERROR: File is too large'

        files = {'file': file1}

        # send file to worker
        response = requests.post(WORKER_IP, files=files)
        return response.text

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)