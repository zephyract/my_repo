#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import cv2
import numpy as np
import random
from random import gauss as gauss
from pprint import pprint
from math import pow
import pdb

class Image(object):
    def __init__(self, file):
        self.img = cv2.imread(file)
        self.H, self.W, _ = self.img.shape
        self.sum = self.img.size / _
        self.showImage("Original.jpeg", self.img)

    def showImage(self, name, img):
        print "Press s to save this picture or others to exit.\n" 
        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)

        if key == ord('s'):
            cv2.imwrite(name, img)

    def gaussNoise(self, means, sigma):
        out = self.img.copy()
        for x in xrange(self.W):
            for y in xrange(self.H):
                p0 = (int(gauss(means, sigma)) & 0xff + out[x, y][0])
                p1 = (int(gauss(means, sigma)) & 0xff + out[x, y][1])
                p2 = (int(gauss(means, sigma)) & 0xff + out[x, y][2])
                
                out[x, y] = (p0, p1, p2)

        self.showImage("gaussNoise.jpeg", out)

    def saltAndPepper(self, SNR):
        out = self.img.copy()
        cnt = int(self.sum * SNR)

        for i in xrange(cnt):
            #  pdb.set_trace()
            randX = random.choice(range(self.W - 1))
            randY = random.choice(range(self.H - 1))

            out[randY, randX] = random.choice([(0, 0, 0), (0xff, 0xff, 0xff)])
            
        self.showImage("saltAndPepper.jpeg", out)

    def arithMean(self):
        out = self.img.copy()
        mask = np.ones((3, 3)).astype(int)
        b, g, r = cv2.split(out)
        #  pprint(b)
        for x in xrange(self.W - 3):
            for y in xrange(self.H - 3):
                #  pdb.set_trace()
                mat = b[x: x + 3, y: y + 3]
                pb = np.abs(np.sum(mat * mask)) / 9
                mat = g[x: x + 3, y: y + 3]
                pg = np.abs(np.sum(mat * mask)) / 9
                mat = r[x: x + 3, y: y + 3]
                pr = np.abs(np.sum(mat * mask)) / 9

                out[x, y] = (pb, pg, pr)

        self.showImage("arithMean.jpeg", out)

    def geomeMean(self):
        mask = np.ones((3, 3))
        out = self.img.copy()
        b, g, r = cv2.split(out)

        for x in xrange(self.W - 3):
            for y in xrange(self.H - 3):
                mat = b[x: x + 3, y: y + 3]
                pb = np.power(np.prod(mat), 1.0 / 9)
                mat = g[x: x + 3, y: y + 3]
                pg = np.power(np.prod(mat), 1.0 / 9)
                mat = r[x: x + 3, y: y + 3]
                pr = np.power(np.prod(mat), 1.0 / 9)

                out[x, y] = (pb, pg, pr)

        self.showImage("geomeMean.jpeg", out)

    def harmoMean(self):
        out = self.img.copy()
        b, g, r = cv2.split(out)
        mask = np.ones((3, 3))

        for x in xrange(self.W - 3):
            for y in xrange(self.H - 3):
                mat = b[x: x + 3, y: y + 3]
                mat = mask / mat
                pb = int(float(9 / np.abs(np.sum(mat * mask))))
                mat = g[x: x + 3, y: y + 3]
                mat = mask / mat
                pg = int(float(9 / np.abs(np.sum(mat * mask))))
                mat = r[x: x + 3, y: y + 3]
                mat = mask / mat
                pr = int(float(9 / np.abs(np.sum(mat * mask))))
                
                out[x, y] = (pb, pg, pr)

        self.showImage("harmoMean.jpeg", out)

    def reHarmoMead(self, Q):
        out = self.img.copy()
        b, g, r = cv2.split(out)
        
        for x in xrange(self.W - 3):
            for y in xrange(self.H - 3):
                if Q >= 0:
                    mat1 = np.power(b[x: x + 3, y: y + 3], Q)
                    mat2 = np.power(b[x: x + 3, y: y + 3], Q + 1)
                    pb = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))
                    mat1 = np.power(g[x: x + 3, y: y + 3], Q)
                    mat2 = np.power(g[x: x + 3, y: y + 3], Q + 1)
                    pg = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))
                    mat1 = np.power(r[x: x + 3, y: y + 3], Q)
                    mat2 = np.power(r[x: x + 3, y: y + 3], Q + 1)
                    pr = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))
    
                    out[x, y] = (pb, pg, pr)
    
                else:
                    pass
                    #  pdb.set_trace()
                    #  mat1 = b[x: x + 3, y: y + 3]
                    #  mat2 = b[x: x + 3, y: y + 3]
                    #  for xx in xrange(x, x + 3):
                        #  for yy in xrange(y, y + 3):
                            #  mat1[xx - x, yy - y] = pow(mat1[xx - x, yy - y], Q)
                            #  mat2[xx - x, yy - y] = pow(mat2[xx - x, yy - y], Q + 1)
                    #  pb = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))
                    #  mat1 = g[x: x + 3, y: y + 3]
                    #  mat2 = g[x: x + 3, y: y + 3]
                    #  for xx in xrange(x, x + 3):
                        #  for yy in xrange(y, y + 3):
                            #  mat1[xx - x, yy - y] = pow(mat1[xx - x, yy - y], Q)
                            #  mat2[xx - x, yy - y] = pow(mat2[xx - x, yy - y], Q + 1)
                    #  mat1 = r[x: x + 3, y: y + 3]
                    #  mat2 = r[x: x + 3, y: y + 3]
                    #  pg = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))
                    #  for xx in xrange(x, x + 3):
                        #  for yy in xrange(y, y + 3):
                            #  mat1[xx - x, yy - y] = pow(mat1[xx - x, yy - y], Q)
                            #  mat2[xx - x, yy - y] = pow(mat2[xx - x, yy - y], Q + 1)
                    #  pr = int(float(np.abs(np.sum(mat1)) / np.abs(np.sum(mat2))))

        self.showImage("reHarmoMead.jpeg", out)

if __name__ == "__main__":
    #  img = Image("./test.jpeg")
    #  img.gaussNoise(0, 1)
    #  img.saltAndPepper(0.3)
    img = Image("./saltAndPepper.jpeg")
    #  img.arithMean()
    #  img.geomeMean()
    #  img.harmoMean()
    img.reHarmoMead(1)
    #  img.reHarmoMead(-2)
