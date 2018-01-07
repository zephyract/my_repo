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
        self.page.append(False)
        line = stdin.readline()
        #tasks存储请求序列
        self.tasks = [int(i) for i in line.split(",")]
        self.ans = ""
        self.pageFault = 0
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

            self.ans += (str(int(self.page[-1])) + r"/")

    def OPT(self):
        #  pdb.set_trace()
        for idx, t in enumerate(self.tasks):
            #  if idx == 10:
                #  pdb.set_trace()
            hit = t in self.page
            if not hit:
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
            hit = t in self.page
            if not hit:
                self.pageFault += 1
                self.page[idx] = t

            self.page[-1] = hit
            self.getAns()
            idx = (idx + 1) % self.size if not hit else idx

        self.getAns(True)

    def LRU(self):
        pass
           
if __name__ == "__main__":
    lab3 = Memory()
    method = (lab3.OPT, lab3.FIFO, lab3.LRU)
    method[lab3.method - 1]()

