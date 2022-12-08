from flask import Flask, request
from imgprocess import ImgModel
app = Flask(__name__)
model = ImgModel()

HOST_IP = "172.17.3.8"
 
@app.route('/process', methods=['POST'])
def classify():
    print("request = ", request)
    if 'file' not in request.files:
        # this is a problem
        return "BAD REQUEST"
    request.files['file'].save("tmp.jpg")
    return model.process("tmp.jpg") + "-" + HOST_IP

if __name__ == '__main__':
    app.run(host=HOST_IP, port=9000)
