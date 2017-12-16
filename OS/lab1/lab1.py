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
            if line == "" or line == "exit\n":
                break
            d = {}
            d["id"], d["st"], d["runtime"], d["priority"], d["time"] = [int(i.strip()) for i in line.split(r"/")]
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
        inThread = sorted(self.T, key = lambda x: x["st"])
        #  pprint(inThread)
        self.getAns(inThread)

    def SJF(self):
        inThread = sorted(self.T, key = lambda x: (x["st"], x["runtime"]))
        pprint(inThread)
        #  pdb.set_trace()
        self.getAns(inThread)


if __name__ == "__main__":
    test = Threads()
    method = (test.FCFS, test.SJF)
    #  pdb.set_trace()
    method[test.method - 1]()
