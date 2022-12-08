import os
from flask import Flask, request
# for model
from timing import Logger
import requests

HOST = "192.171.20.121" # Server IP (change it to your server IP)
WORKERS = ["172.17.3.8", "172.17.3.13", "172.17.3.16"] # Worker IPs (change it to your worker IPs)

WORKER_IP1 = 'http://{}:9000/process'.format(WORKERS[0])
WORKER_IP2 = 'http://{}:9000/process'.format(WORKERS[1])
WORKER_IP3 = 'http://{}:9000/process'.format(WORKERS[2])

workers = [WORKER_IP1, WORKER_IP2, WORKER_IP3]

current_worker = 0

app = Flask(__name__)
timing = Logger()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    
    global current_worker

    if request.method == 'POST':

        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        
        file1 = request.files['file1']

        file1.seek(0, os.SEEK_END)
        length = file1.tell()
        file1.seek(0)

        if not (file1.content_type == 'image/jpeg' or file1.content_type == 'image/png'):
            return 'ERROR: File must be in .png or .jpg format.'
        elif (file1.content_length > 10000000):
            return 'ERROR: File is too large'

        t = timing.starttiming(file1.filename, length)

        files = {'file': file1}
        
        WORKER_IP = workers[current_worker]
        current_worker = (current_worker + 1) % (len(workers))
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
    app.run(host=HOST, port=8000)
