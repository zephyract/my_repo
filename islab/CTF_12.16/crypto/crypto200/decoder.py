#!/usr/bin/env python2

import random
import string
import pdb

def re_rot13(s):
    return s.translate(string.maketrans(string.uppercase[13: ] + string.uppercase[: 13] + string.lowercase[13: ] + string.lowercase[: 13], string.uppercase + string.lowercase))

def re_base64(s):
    #  return ''.join(s.encode('base64').split())
    return s.decode("base64")

def re_hex(s):
    #  return s.encode('hex')
    return s.decode("hex")

def re_upsidedown(s):
    return s.translate(string.maketrans(string.lowercase + string.uppercase,
            string.uppercase + string.lowercase))

flag = 'FLAG{.....................}'  # try to recover flag

E = (re_rot13, re_base64, re_hex, re_upsidedown)

#  for i in range(random.randint(30, 50)):
    #  print i
    #  c = random.randint(0, len(E) - 1)
    #  flag = '%d%s' % (c, E[c](flag))

#  open('flag.enc', 'w').write(flag)
with open("flag.enc") as f:
    flag = f.read()

while True:
    #  pdb.set_trace()
    c = int(flag[0])
    flag = E[c](flag[1: ])
    if "FLAG" in flag:
        print flag
        break
