#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from libnum import prime_test as isPrime
from libnum import generate_prime as genPrime
from libnum import gcd, xgcd
from libnum import n2s, s2n
from gmpy2 import invert

def encrypt():
    m = raw_input("请输入明文: ")
    p = genPrime(1024)
    q = genPrime(1024)
    n = p * q
    fi = (p- 1) * (q - 1)
    i = (p - 1) * (q - 1) - 1
    while True:
        if gcd(i, (p - 1) * (q - 1)) == 1:
            e = i
            break
        i -= 1

    c = pow(s2n(m), e, n)
    print "密文: ",  c
    return p, q, n, e, c

def decrypt(p, q, e, c):
    d = invert(e, (p - 1) * (q - 1))
    m = pow(c, d, n)
    print "解密: ", n2s(m)

    
if __name__ == "__main__":
    p, q, n, e, c = encrypt()
    decrypt(p, q, e, c)
