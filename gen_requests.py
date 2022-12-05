import sys
import threading
import _thread
import time
import requests
import numpy.random as r

def req(ip):
    # sends one request
    charseq = list(range(65, 91)) + list(range(97, 123))
    rString = ''.join(map(chr, r.choice(charseq, 5, replace=True)))
    requests.get(ip, data={'text': rString})
    _thread.interrupt_main()

# args: # total request, max. concurrent requests
if len(sys.argv) > 3:
    ip = sys.argv[1]
    total = sys.argv[2]
    max = sys.argv[3]

    # start threads
    out = 0
    while (total > 0):
        try:
            if (out > max):
                time.sleep(0.5)
            else:
                t = threading.Thread(target=req, args=(ip))
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
