import sys
import hashlib
import itertools
import threading
import _thread
import time

def crack(start, chars, hash, ret, ret_index):
    # checks partition of password space beginning with 'start' for a match
    for p in itertools.product([start], chars, chars, chars, chars):
        if hashlib.md5(bytearray(p)).hexdigest() == hash:
            # we found a match
            m = ''.join(map(chr, p))
            ret[ret_index] = m
            _thread.interrupt_main()
    _thread.interrupt_main()
            

# first command-line argument is interpreted as a hash to crack
# anything else is ignored
if len(sys.argv) > 1:
    hash = sys.argv[1]
    if len(hash) != 32:
        print('ERROR: not a valid MD5 hash')
        exit(-1)
    # A - Z : 65 - 90
    # a - z : 97 - 122
    charseq = list(range(65, 91)) + list(range(97, 123))

    start = time.time()

    # start threads
    thread_count = 0
    ret = [None] * len(charseq)
    for i,s in enumerate(charseq):
        t = threading.Thread(target=crack, args=(s, charseq, hash, ret, i), daemon=True)
        t.start()
        thread_count += 1

    # wait for threads to return: each one will raise an exception
    while True:
        try:
            if thread_count == 0:
                break
            time.sleep(0.5)
        except KeyboardInterrupt:
            # something finished
            for res in ret:
                if res != None:
                    print(f'Match: {res}')
                    end = time.time()
                    print(f'Took {end - start} seconds')
                    exit(0)
            else:
                thread_count -= 1

    print('ERROR: hash not in space of 5-character alphabetic passwords')
    end = time.time()
    print(f'Took {end - start} seconds')
    exit(-1)
else:
    print('Arguments: hash')
    exit(-1)
