import hashlib
import sys
import threading
import _thread
import time
import requests
import numpy as np
from timing import Logger
random = np.random.RandomState(372189)

logger = Logger()

def req(ip):
    # sends one request
    charseq = list(range(65, 91)) + list(range(97, 123))
    spassword = ''.join(map(chr, random.choice(charseq, 5, replace=True)))
    #password = random.choice(["AAAAA", "BBBBB", "AAABB", "AAAAB", "AABBB"])
    
    password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    url = 'http://' + ip + '/break_hash/' + password_hash
    
    idx = logger.starttiming(password_hash)
    r = requests.get(url)
    logger.stoptiming(idx, r.text)

    print(r.text)
    _thread.interrupt_main()

# args: # total request, max. concurrent requests
if len(sys.argv) > 3:
    ip = sys.argv[1]
    total = eval(sys.argv[2])
    max = eval(sys.argv[3])

    # start threads
    out = 0
    while (total > 1):
        try:
            if out >= max:
                time.sleep(0.5)
            else:
                t = threading.Thread(target=req, args=(ip,))
                t.start()
                out += 1
        except KeyboardInterrupt:
            # one of the requests finished
            total -= 1
            out -= 1

    print("All requests finished")
else:
    print('Arguments: ip, total_reqs, max_concurrent')
    exit(-1)
