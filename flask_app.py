import os
from flask import Flask, request
# for model
from model import run_model
import socket
import requests

WORKER_IP1 = 'http://172.17.2.14:5000/process'
WORKER_IP2 = 'http://172.17.2.17:5000/process'
WORKER_IP3 = 'http://172.17.2.23:5000/process'

workers = [WORKER_IP1, WORKER_IP2, WORKER_IP3]

current_worker = 0

HOST = 'pcvm2-9.instageni.cenic.net'
UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    
    global current_worker

    if request.method == 'POST':

        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)

        # file1.save(path)

        # after getting and saving file, run model on it
        # model_results = run_model(path)

	# create connection with worker, make this more generic later
        # round-robin scheduling

        '''
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('172.17.2.14', 8500))

        file = open(path, 'rb')

        image_data = file.read(2048)

        while image_data:
            client.send(image_data)
            image_data = file.read(2048)

        # model_results = client.recv(2048)
        
        model_results = ''

        client.close()
        file.close()

        # show model results to user
        return model_results
        '''

        if not (file1.content_type == 'image/jpeg' or file1.content_type == 'image/png'):
            return 'ERROR: File must be in .png or .jpg format.'
        elif (file1.content_length > 10000000):
            return 'ERROR: File is too large'

        files = {'file': file1}
        
        WORKER_IP = workers[current_worker]
        current_worker = (current_worker + 1) % (len(workers))
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
    app.run(host=HOST, port=8000)
