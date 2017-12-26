#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from sys import stdin
from copy import deepcopy
from pprint import pprint
import pdb

class Memory(object):
    def __init__(self):
        self.opId = 1
        self.method = int(stdin.readline())
        self.size = int(stdin.readline())
        self.memory = []
        chunk = {"st": 0, "ed": self.size - 1, "pid": -1, "size": self.size}
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
        ans = str(self.opId)
        self.memory = sorted(self.memory, key = lambda x: x["st"])
        for i in self.memory:
            if i["pid"] == -1:
                ans += (r"/" + str(i["st"]) + "-" + str(i["ed"]) + ".0")
            else:
                ans += (r"/" + str(i["st"]) + "-" + str(i["ed"]) + ".1." + str(i["pid"]))

        self.opId += 1
        print ans

    def free(self, pid):
        for c in self.memory:
            if c["pid"] == pid:
                c["pid"] = -1
                break

        idx = 0
        while True:#合并相邻空闲chunk
            try:
                if self.memory[idx]["pid"] == self.memory[idx + 1]["pid"] == -1:
                    self.memory[idx]["ed"] = self.memory[idx + 1]["ed"]
                    self.memory[idx]["size"] = self.memory[idx]["ed"] - self.memory[idx]["st"] + 1
                    del self.memory[idx + 1]

                idx += 1
            except:
                self.getAns()
                break

    def malloc(self, method, i):
        idx = 0
        if method == "firstFit":
            self.memory = sorted(self.memory, key = lambda x: x["st"])
        elif method == "bestFit":
            self.memory = sorted(self.memory, key = lambda x: x["size"])
        elif method == "worstFit":
            self.memory = sorted(self.memory, key = lambda x: x["size"], reverse = True)
        
        while True:
            try:
                if self.memory[idx]["pid"] == -1 and self.memory[idx]["size"] > i["size"]:
                    #分割空闲块
                    c1 = deepcopy(self.memory[idx])
                    c1["pid"] = i["pid"]
                    c1["ed"] = i["size"] + c1["st"] - 1
                    c1["size"] = i["size"]
            
                    #空闲chunk存在剩余
                    if c1["ed"] < self.memory[idx]["ed"]:
                        c2 = {}
                        c2["st"] = c1["ed"] + 1
                        c2["ed"] = self.memory[idx]["ed"]
                        c2["pid"] = -1
                        c2["size"] = c2["ed"] - c2["st"] + 1
                        self.memory = self.memory[:idx] + [c1, c2] + self.memory[idx + 1:]
                        self.getAns()
                        break
            
                    else:
                        self.memory = self.memory[:idx] + [c1] + self.memory[idx + 1:]
                        self.getAns()
                        break
                idx += 1 
            except:
                break

    def firstFit(self):
        #  pdb.set_trace()
        for i in self.ops:
            #  if i["id"] == 8:
                #  pdb.set_trace()
            if i["op"] == 1:#申请
                self.malloc("firstFit", i)
            else:#释放
                #  pdb.set_trace()
                self.free(i["pid"])

    def bestFit(self):
        for i in self.ops:
            if i["op"] == 1:
                self.malloc("bestFit", i)
            else:
                self.free(i["pid"])

    def worstFit(self):
        for i in self.ops:
            if i["op"] == 1:
                self.malloc("worstFit", i)
            else:
                self.free(i["pid"])

if __name__ == "__main__":
    lab2 = Memory()
    method = (lab2.firstFit, lab2.bestFit, lab2.worstFit)
    method[lab2.method - 1]()
