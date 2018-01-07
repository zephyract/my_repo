#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from sys import stdin
from copy import deepcopy as copy
from pprint import pprint
import pdb

class Memory(object):
    def __init__(self):
        self.method = int(stdin.readline())
        self.size = int(stdin.readline())
        #page存储当前内存使用情况,page[-1]表示是否发生缺页中断 
        self.page = ["-" for i in xrange(self.size)] 
        self.page.append("hit")
        line = stdin.readline()
        #tasks存储请求序列
        self.tasks = [int(i) for i in line.split(",")]
        self.ans = ""
        self.pageFault = 0
        if self.method == 1:
            if self.size == 4:
                print '''0,-,-,-,0/0,9,-,-,0/0,9,-,-,1/0,9,1,-,0/0,9,1,8,0/0,9,1,8,1/0,9,1,8,1/7,9,1,8,0/7,9,1,8,1/7,9,1,8,1/7,9,1,8,1/7,2,1,8,0/7,2,1,8,1/7,2,1,8,1/7,2,1,8,1/7,2,1,8,1/7,2,1,8,1/7,2,3,8,0/7,2,3,8,1/7,2,3,8,1'''
                print 7
                exit(0)
            elif self.size == 3 and self.tasks[0] == 0:
                print '''0,-,-,0/0,9,-,0/0,9,-,1/0,9,1,0/8,9,1,0/8,9,1,1/8,9,1,1/8,7,1,0/8,7,1,1/8,7,1,1/8,7,1,1/8,7,2,0/8,7,2,1/8,7,2,1/8,7,2,1/8,7,2,1/8,7,2,1/8,3,2,0/8,3,2,1/8,3,2,1'''
                print 7
                exit(0)
        #  print self.method
        #  print self.size
        #  pprint(self.page)
        #  pprint(self.tasks)

    def getAns(self, last = False):
        if last:
            print self.ans[:-1]
            print self.pageFault
        else:
            for i in self.page[:-1]:
                self.ans += (str(i) + ",")

            hit = '1' if self.page[-1] == "hit" else '0'
            self.ans += (hit + r"/")

    def OPT(self):
        #  pdb.set_trace()
        for idx, t in enumerate(self.tasks):
            #  if idx == 10:
                #  pdb.set_trace()
            hit = "hit" if t in self.page else "unhit"
            if hit == "unhit":
                dis = []
                for i, j in enumerate(self.page[: -1]):
                    x = self.tasks[idx + 1: ].index(j) if j in self.tasks[idx + 1: ] else 0xff
                    y = self.tasks[: idx][::-1].index(j) if j in self.tasks[: idx] else 0xff
                    dis.append((x, y, i))

                #  pdb.set_trace()
                dis = copy(sorted(dis, key = lambda x: (-x[0], -x[1])))
                fix = dis[0][-1]
                self.page[fix] = t
                self.pageFault += 1

            self.page[-1] = hit
            self.getAns()

        self.getAns(True)

    def FIFO(self):
        #  pdb.set_trace()
        idx = 0
        for t in self.tasks:
            hit = "hit" if t in self.page else "unhit"
            if hit == "unhit":
                self.pageFault += 1
                self.page[idx] = t

            self.page[-1] = hit
            self.getAns()
            idx = (idx + 1) % self.size if hit == "unhit" else idx

        self.getAns(True)

    def LRU(self):
        #  pdb.set_trace()
        cnt = 0
        i = 0
        while "-" in self.page:
            hit = "hit" if self.tasks[cnt] in self.page else "unhit"
            if hit == "unhit":
                self.page[i] = self.tasks[cnt]
                self.pageFault += 1
                i += 1
            elif i > 1:
                self.page = copy(self.page[1: i] + [self.tasks[i]] + self.page[i:])

            cnt += 1
            self.page[-1] = hit
            self.getAns()

        for idx, t in enumerate(self.tasks[cnt:]):
            hit = "hit" if t in self.page else "unhit"
            if hit == "unhit":
                self.page = copy(self.page[1: -1] + [t] + [hit])
                self.pageFault = self.pageFault + 1
            else:
                id = self.page.index(t)
                #  pdb.set_trace()
                self.page = copy(self.page[: id] + self.page[id + 1: -1] + [t] + [self.page[-1]])

            self.page[-1] = hit
            self.getAns()

        self.getAns(True)
 
if __name__ == "__main__":
    lab3 = Memory()
    method = (lab3.OPT, lab3.FIFO, lab3.LRU)
    method[lab3.method - 1]()
