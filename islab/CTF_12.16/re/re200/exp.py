#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
import pdb
from time import sleep
from string import printable
#  context.log_level = "debug"

dic = printable
flag = "flag{"

while True:
    for i in dic:
        #  if i == "H":
            #  pdb.set_trace()
        io = process("./bug")
        #  io.sendlineafter("flag: ", flag + i)
        io.sendline(flag + i)
        if io.recvline()[-2] != '!':
            io.close()
        else:
            flag += i
            print flag
            if flag[-1] == "}":
                exit(0)
            #  sleep(3)
            break
