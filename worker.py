import sys
import hashlib
import itertools

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

    for p in itertools.product(charseq, repeat=5):
        if hashlib.md5(bytearray(p)).hexdigest() == hash:
            # we found a match
            m = ''.join(map(chr, p))
            print(f'Match: {m}')
            exit(0)

    # no match
    print('ERROR: hash not in space of 5-character alphabetic passwords')
    exit(-1)
else:
    print('Arguments: hash')
    exit(-1)
