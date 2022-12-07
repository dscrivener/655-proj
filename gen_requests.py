import os
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
    files_dir = os.listdir('./images')

    filename = np.random.choice(files_dir)
    pathname = './images/' + filename
    idx = logger.starttiming(filename, os.path.getsize(pathname))

    # infer MIME type from extension
    if (filename.split('.')[1] == 'png'):
        mime = 'image/png'
    elif (filename.split('.')[1] == 'jpg' or filename.split('.')[1] == 'jpeg'):
        mime = 'image/jpeg'
    else:
        mime = 'error'

    file = open(pathname, 'rb')
    files_req = {'file1': (filename, file, mime)}
    r = requests.post(ip, files=files_req)

    logger.stoptiming(idx, r.text)
    print(r.text)
    _thread.interrupt_main()

# args: ip, total requests, max. concurrent requests
if len(sys.argv) > 3:
    ip = sys.argv[1]
    print(ip)
    total = eval(sys.argv[2])
    max = eval(sys.argv[3])

    # start threads
    out = 0
    while (total > 0):
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
