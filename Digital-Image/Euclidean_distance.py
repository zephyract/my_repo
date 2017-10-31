#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from math import pow, sqrt
import re

def get_points():
    pattern = re.compile(r"[-+]?\d+[.]?\d*")

    while True:
        p1 = raw_input("Please input point x: ")
        l1 = pattern.findall(p1)
        if len(l1) != 3:
            print "Invalid Input! Try again!"
            continue
        else:
            l1 = tuple([float(i) for i in l1])
            break
    while True:
        p2 = raw_input("Please input point y: ")
        l2 = tuple(pattern.findall(p2))                    
        if len(l2) != 3:
            print "Invalid Input! Try again!"
            continue
        else:
            l2 = tuple([float(i) for i in l2])
            break

    return l1, l2

def calculate(p1, p2):
    dx = float(p1[0]) - float(p2[0])
    dy = float(p1[1]) - float(p2[1])
    dz = float(p1[2]) - float(p2[2])

    return sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))

if __name__ == "__main__":
    while True:
        p1, p2 = get_points()
        print '''The Euclidean Distance between''', p1, "and", p2, "is %f" % calculate(p1, p2)
        if raw_input("Type EXIT to exit program.\n") == "EXIT":
            break
