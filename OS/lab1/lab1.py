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
            d["id"], d["st"], d["runtime"], d["priority"], d["timeslice"] = [int(i.strip()) for i in line.split(r"/")]
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

    def RR(self):
        inThread = sorted(self.T, key = lambda x: x["st"])
        for i in inThread:
            i["remain"] = i["runtime"]

        timeTable = []
        timeSlice = inThread[0]["timeslice"]
        ii = 0
        T = sum([i["runtime"] for i in inThread])
        while True:
            timeTable.append(timeSlice * ii)
            ii += 1
            if timeTable[-1] >= T:
                timeTable = timeTable[: -1]
                break

        #  print "flag"
        timeTable.append(T)
        #  pprint(timeTable)
        cnt = inThread[-1]["id"]

        idx = 0
        id = 0#id + 1为pid
        outThread = []
        while True:
            t = timeTable[idx]
            if t == timeTable[-1]:
                #  pdb.set_trace()
                break
            #  if len(outThread) >= 10:
                #  break

            #  print "flag"
            #  self.getAns(outThread)
            inThread = sorted(inThread, key = lambda x: x["st"])
            tmp = 0
            while True:
                if inThread[id]["remain"] and inThread[id]["st"] <= t:
                    break
                id = (id + 1) % cnt

            if inThread[id]["remain"] and inThread[id]["st"] <= t:
                tmp = deepcopy(inThread[id])
                tmp["st"] = t
                if inThread[id]["remain"] >= timeSlice:
                    tmp["runtime"] = timeSlice
                    inThread[id]["remain"] -= timeSlice
                    outThread.append(tmp)
                else:
                    tmp["runtime"] = tmp["remain"]
                    inThread[id]["remain"] = 0
                    outThread.append(tmp)
                    timeTable = timeTable[: idx + 1] + [timeTable[idx] + tmp["runtime"]] + timeTable[idx + 1:]
            
                #  if idx == 6:
                    #  pdb.set_trace()
                id = (id + 1) % cnt
                idx += 1

        #  pprint(outThread)
        self.getAns(outThread)

    def DP(self):
        inThread = sorted(self.T, key = lambda x: x["st"])
        for i in inThread:
            i["remain"] = i["runtime"]

        timeTable = []
        timeSlice = inThread[0]["timeslice"]
        T = sum([i["runtime"] for i in inThread])

        ii = 0
        while True:
            timeTable.append(timeSlice * ii)
            ii += 1
            if timeTable[-1] >= T:
                timeTable = timeTable[: -1]
                break
        timeTable.append(T)

        idx = 0
        outThread = []
        while True:
            t = timeTable[idx]
            if t == timeTable[-1]:
                break

            #  if len(outThread) >= 8:
                #  break

            pdb.set_trace()
            inThread = sorted(inThread, key = lambda x: (x["priority"], x["st"]))
            for i in inThread:
                if i["remain"] and i["st"] <= t:
                    i["used"] = True
                    i["priority"] += 3
                    tmp = deepcopy(i)
                    tmp["st"] = t
                    if tmp["remain"] >= timeSlice:
                        tmp["runtime"] = timeSlice
                        i["remain"] -= timeSlice
                        outThread.append(tmp)
                    else:
                        tmp["runtime"] = tmp["remain"]
                        i["remain"] = 0
                        outThread.append(tmp)
                        timeTable = timeTable[: idx + 1] + [timeTable[idx] + tmp["runtime"]] + timeTable[idx + 1:]

                    idx += 1
                    break

            for i in inThread:
                if i["used"] == True:
                    i["used"] = False
                else:
                    #优先级最高为0
                    i["priority"] = 0 if i["priority"] - 1 <= 0 else i["priority"] - 1

        self.getAns(outThread)
        

if __name__ == "__main__":
    lab1 = Threads()
    method = (lab1.FCFS, lab1.SPF, lab1.SRF, lab1.RR, lab1.DP)
    #  pdb.set_trace()
    method[lab1.method - 1]()
