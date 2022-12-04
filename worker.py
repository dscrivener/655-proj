import hashlib
import itertools
import socket

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
            # we found a match
            m = ''.join(map(chr, p))
            print(f'Match: {m}')
            return m

    # no match
    print('ERROR: hash not in space of 5-character alphabetic passwords')
    return None

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                hash = conn.recv(1024) #receiving hash data
                if not hash:
                    break
                if len(hash) != 32:
                    print('ERROR: not a valid MD5 hash')
                    break

                match = crack_hash(hash.decode("utf-8")) #cracking hash
                if match is None:
                    conn.sendall("ERROR: hash not in space of 5-character alphabetic passwords".encode())
                else:
                    conn.sendall(match.encode())