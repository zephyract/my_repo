#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from sys import stdin
from pprint import pprint
from time import sleep
from copy import deepcopy
import pdb

class Threads(object):
    def __init__(self):
        self.method = int(stdin.readline())
        self.T = []
        while True:
            line = stdin.readline()
            if line == "" or line == "\n":
                break
            d = {}
            d["id"], d["st"], d["runtime"], d["priority"], d["time"] = [int(i.strip()) for i in line.split(r"/")]
            d["used"] = False
            #  print d
            self.T.append(d)

        #  print self.method
        #  pprint(self.T)

    def getAns(self, inThread):
        ans = []
        for i,j in enumerate(inThread):
            d = {}
            d["seq"], d["id"], d["priority"], d["runtime"] = (i + 1, j["id"], j["priority"], j["runtime"])
            d["st"] = ans[i - 1]["ed"] if i else 0
            d["ed"] = d["st"] + d["runtime"]
            ans.append(d)

        for i in ans:
            print "%d/%d/%d/%d/%d" % (i["seq"], i["id"], i["st"], i["ed"], i["priority"])

    def FCFS(self):
        outThread = sorted(self.T, key = lambda x: x["st"])
        #  pprint(outThread)
        self.getAns(outThread)

    def SPF(self):
        inThread = sorted(self.T, key = lambda x: x["runtime"])
        time = 0
        outThread = []
        for i in xrange(len(self.T)):
            #  pprint(inThread)
            #  print ""
            for j in inThread:
                if j["st"] <= time and not j["used"]:
                    time += j["runtime"]
                    j["used"] = True
                    outThread.append(j)
                    break
        #  pdb.set_trace()
        self.getAns(outThread)

    def SRF(self):
        inThread = sorted(self.T, key = lambda x: x["st"])
        for i in inThread:
            i["remain"] = i["runtime"]

        timeTable = [i["st"] for i in inThread]
        timeTable.append(sum([i["runtime"] for i in inThread]))
        timeTable.append(sum([i["runtime"] for i in inThread]))#多加一次总时间方便处理

        outThread = []
        idx = 0
        while True:
            t = timeTable[idx]
            if t == timeTable[-1]:
                break

            inThread = sorted(inThread, key = lambda x: x["remain"])
            for i in inThread:
                #  pdb.set_trace()
                if i["remain"] and i["st"] <= t:
                    #bug: 出现相同键值对完全相同的字典时,修改对所有字典起作用
                    #python的引用: http://www.cnblogs.com/Xjng/p/3829368.html
                    tmp = deepcopy(i)
                    tmp["st"] = t
                    if (timeTable[idx + 1] - t) <= i["remain"]:
                        tmp["runtime"] = (timeTable[idx + 1] - t)
                        i["remain"] -= (timeTable[idx + 1] - t)
                        outThread.append(tmp)
                        #  pdb.set_trace()
                    else:
                        tmp["runtime"] = tmp["remain"]
                        i["remain"] = 0
                        outThread.append(tmp)
                        timeTable = timeTable[: idx + 1] + [timeTable[idx] + tmp["runtime"]] + timeTable[idx + 1:]
                        #  pdb.set_trace()

                    idx += 1
                    break
        
        #  pprint(outThread)
        self.getAns(outThread)

if __name__ == "__main__":
    lab1 = Threads()
    method = (lab1.FCFS, lab1.SPF, lab1.SRF)
    #  pdb.set_trace()
    method[lab1.method - 1]()
