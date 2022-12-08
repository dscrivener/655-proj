import sys
import constants
from flask import Flask, request
import requests
import socket
from imgprocess import ImgModel
from io import BytesIO
app = Flask(__name__)
model = ImgModel()

HOST_IP = '172.17.2.14'
 
@app.route('/process', methods=['POST'])
def classify():
    print("request = ", request)
    if 'file' not in request.files:
        # this is a problem
        return "BAD REQUEST"
    request.files['file'].save("tmp.jpg")
    return model.process("tmp.jpg") + "-" + HOST_IP

if __name__ == '__main__':
    if len(sys.argv) == 2:
        HOST_ID = eval(sys.argv[1])
        if HOST_ID > 0 & HOST_ID < 4:
            HOST_IP = constants.WORKERS[HOST_ID - 1]
            app.run(host=HOST_IP, port=9000)
        else:
            print("Invalid worker id - Expected 1, 2, or 3")
