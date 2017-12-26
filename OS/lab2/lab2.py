#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from sys import stdin
from copy import deepcopy
from pprint import pprint
import pdb

class Memory(object):
    def __init__(self):
        self.method = int(stdin.readline())
        self.size = int(stdin.readline())
        self.memory = []
        chunk = {"st": 0, "ed": self.size, "pid": -1}
        self.memory.append(chunk)

        self.ops = []
        while True:
            line = stdin.readline()
            if line == "" or line == "\n":
                break
            op = {}
            op["id"], op["pid"], op["op"], op["size"] = [int(i.strip()) for i in line.split(r"/")]
            self.ops.append(op)
        
        #  pprint(self.memory)
        #  pprint(self.ops)

    def getAns(self):
        id = 1
        for i in self.memory:
            ans = str(id)
            if i["pid"] == -1:
                ans += (r"/" + str(i["st"] + "-" + str(i["ed"] + ".0")))
            else:
                ans += (r"/" + str(i["st"] + "-" + str(i["ed"] + ".1." + str(i["pid"]))))

            id += 1
            print ans

    def firstFit(self):
        for i in self.ops:
            if i["op"] == 1:#申请


    def bestFit(self):

    def worstFit(self):


if __name__ == "__main__":
    lab2 = Memory()
    method = (lab2.firstFit, lab2.bestFit, lab2.worstFit)
    method[lab2.method]()
