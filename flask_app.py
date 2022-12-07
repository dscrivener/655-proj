import os
from flask import Flask, request
# for model
from timing import Logger
import socket
import requests

WORKER_IP = 'http://172.17.2.14:5000/process'
HOST = 'pcvm2-9.instageni.cenic.net'

app = Flask(__name__)
timing = Logger()

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        
        file1 = request.files['file1']

        if not (file1.content_type == 'image/jpeg' or file1.content_type == 'image/png'):
            return 'ERROR: File must be in .png or .jpg format.'
        elif (file1.content_length > 10000000):
            return 'ERROR: File is too large'

        t = timing.starttiming(file1.filename, file1.content_length)

        files = {'file': file1}

        # send file to worker
        response = requests.post(WORKER_IP, files=files)
        timing.stoptiming(t, response.text)
        return response.text
    
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
