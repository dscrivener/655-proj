from flask import Flask, request
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

app = Flask(__name__)
 
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Submit"></form>'
 
@app.route("/echo")
def echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.args.get('text', '').encode("utf-8"))
        match = s.recv(1024)
        return '''
        <h2>{}</h2>
        <p align="left"><a href=/ ><button>Try another MD5 Hash</button></a></p>
        '''.format(match.decode("utf-8"))

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
