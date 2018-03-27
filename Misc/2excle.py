#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from time import sleep
import xlwt
import re
import os

excle = xlwt.Workbook(encoding = "ascii")
output = excle.add_sheet("output")
sus = excle.add_sheet("suspicious")
root = os.getcwd()
#  print root

functions = ["LGamma", "gser", "gcf", "QGamma", "QChiSq", "InfoTbl"]
args = ["pe", "pn", "fe", "fn"]

vRow = 6
vCol = 4
blockRow = 8
blockCol = 6

def getSvalue(pe, pn, fe, fn):
    f = lambda x: float(x)

    up = f(fe) / (f(fe) + f(fn))
    down =  f(fe) / (f(fe) + f(fn)) + f(pe) / (f(pe)+ f(pn))

    value = f(up) / f(down)

    return value

def readRes(idx):
    with open("{}/output_version/v{}/res.txt".format(root, idx)) as f:
        s = f.read()
        #  print s
        table = re.findall("\d+", s)

    #  print table
    return table
#  readRes(1)

def writeHeader(idx):
    stR = ((idx - 1) / vCol) * blockRow 
    stC = ((idx - 1) % vCol) * blockCol

    output.write(stR, stC, "V{}".format(idx))

    for r in xrange(blockRow - 2):
        output.write(stR + r + 1, stC, functions[r])

    for c in xrange(blockCol - 2):
        output.write(stR, stC + c + 1, args[c])

    if idx == 1:
        for i in xrange(len(functions)):
            sus.write(0, i + 1, functions[i])

    if idx != vRow * vCol:
        sus.write(idx , 0, "v{}".format(idx))

def writeContent(idx):
    stR = ((idx - 1) / vCol) * blockRow + 1
    stC = ((idx - 1) % vCol) * blockCol + 1
    table = readRes(idx)
    
    for r in xrange(len(functions)):
        for c in xrange(len(args)):
            wr = stR + r
            wc = stC + c
            cnt = table[r * len(args) + c]
            output.write(wr, wc, cnt)


        argu = [table[r * len(args) + i] for i in xrange(len(args))]
        #  print argu
        #  sleep(3)
        try:
            svalue = getSvalue(argu[0], argu[1], argu[2], argu[3])
        except ZeroDivisionError:
            svalue = "None"
        sus.write(idx, r + 1, svalue)


if __name__ == "__main__":
    for vr in xrange(vRow):
        for vc in xrange(vCol):
            idx = 4 * vr + vc + 1
            writeHeader(idx)
            if idx != vRow * vCol:
                writeContent(idx)
                print "Version {} 已被写入".format(idx)
                sleep(0.1)
    
    excle.save("{}/out.xlsx".format(root))
