from flask import Flask, request
import requests
import socket
from imgprocess import ImgModel

app = Flask(__name__)
model = ImgModel()
 
@app.route('/process', methods=['POST'])
def classify():
    if 'file1' not in request.files:
        # this is a problem
        return "BAD REQUEST"
    img = request.files['file1']
    return model.process(img)

if __name__ == '__main__':
    app.run()