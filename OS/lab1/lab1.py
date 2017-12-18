#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from sys import stdin
from pprint import pprint
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
        pprint(inThread)
        print timeTable



if __name__ == "__main__":
    lab1 = Threads()
    method = (lab1.FCFS, lab1.SPF, lab1.SRF)
    #  pdb.set_trace()
    method[lab1.method - 1]()
