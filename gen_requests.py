import os
import sys
import threading
import _thread
import time
from joblib import Parallel, delayed
import requests
import numpy as np
from timing import Logger
random = np.random.RandomState(372189)

#logger = Logger()

def req(ip, filename):
    pathname = './images/' + filename

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

# args: ip, total requests, max. concurrent requests
files_dir = os.listdir('./images')

if len(sys.argv) > 3:
    ip = sys.argv[1]
    print(ip)
    total = eval(sys.argv[2])
    max = eval(sys.argv[3])

    candidates = [(ip, files_dir[i % len(files_dir)]) for i in range(total)]

    results = Parallel(n_jobs=max, verbose=10)(delayed(req)(ip, filename) for ip, filename in candidates)

    print("All requests finished")
else:
    print('Arguments: ip, total_reqs, max_concurrent')
    exit(-1)
