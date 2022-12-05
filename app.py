from flask import Flask, request
import socket

PORT = 65432  # The port used by the server
CURRENT_WORKER = 0
#WORKERS = ["172.17.2.17", "172.17.2.23", "172.17.2.24", "172.17.2.22", "172.17.2.14"]
WORKERS = ["172.17.2.14"]

app = Flask(__name__)
 
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Submit"></form>'
 
@app.route("/echo")
def echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        global CURRENT_WORKER
        global WORKERS
        global PORT

        s.connect((WORKERS[CURRENT_WORKER], PORT))
        CURRENT_WORKER = (CURRENT_WORKER + 1) % len(WORKERS)
        s.sendall(request.args.get('text', '').encode("utf-8"))
        match = s.recv(1024)
        return '''
        <h2>{}</h2>
        <p align="left"><a href=/ ><button>Try another MD5 Hash</button></a></p>
        '''.format(match.decode("utf-8"))

@app.route("/break_hash/<hash>")
def break_hash(hash=None):    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        global CURRENT_WORKER
        global WORKERS
        global PORT

        s.connect((WORKERS[CURRENT_WORKER], PORT))
        CURRENT_WORKER = (CURRENT_WORKER + 1) % len(WORKERS)
        s.sendall(hash.encode("utf-8"))
        match = s.recv(1024)
        return match.decode("utf-8")

if __name__ == '__main__':
    app.run(host="204.102.244.60", port=8000)