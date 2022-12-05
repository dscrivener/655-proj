import hashlib
import itertools
import socket
import threading

# Too expensive because it try all possible combinations - 
# have to find a way to finish the execution after finding the match

# from joblib import Parallel, delayed
# def parallel_crack_hash(hash, candidate):
#     if hashlib.md5(bytearray(candidate)).hexdigest() == hash:
#         # we found a match
#         print(f'Match: {candidate}')
#         return candidate

# hash = "594f803b380a41396ed63dca39503542"
# charseq = list(range(65, 91)) + list(range(97, 123))
# results = Parallel(n_jobs=-1, verbose=10)(delayed(parallel_crack_hash)(hash, candidate) for candidate in itertools.product(charseq, repeat=5))
# print(results)

def crack_hash(hash):
    charseq = list(range(65, 91)) + list(range(97, 123))

    for p in itertools.product(charseq, repeat=5):
        if hashlib.md5(bytearray(p)).hexdigest() == hash:
            m = ''.join(map(chr, p))
            print(f'Match: {m}')
            return m

    print('ERROR: hash not in space of 5-character alphabetic passwords')
    return None

HOST = "172.17.2.14"
PORT = 65432

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        while True:
            print("Client address: {}".format(self.client_address))
            hash = self.client_socket.recv(1024)
            if not hash:
                break
            if len(hash) != 32:
                self.client_socket.sendall("ERROR: not a valid MD5 hash".encode())
                break
            match = crack_hash(hash.decode("utf-8"))
            if match is None:
                self.client_socket.sendall("ERROR: hash not in space of 5-character alphabetic passwords".encode())
            else:
                self.client_socket.sendall(match.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
while True:
    server.listen(5)
    client_socket, client_address = server.accept()
    new_thread = ClientThread(client_address, client_socket)
    new_thread.start()
