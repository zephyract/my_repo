#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import numpy as np
from pprint import pprint
import cv2
import pdb

class Image(object):
    def __init__(self, file):
        self.oriImg = cv2.imread(file)
        #  pprint(self.img)
        self.H, self.W, _ = self.oriImg.shape

        self.showImage("Original_Image.jpg", self.oriImg)

    def showImage(self, name, img):
        print "Press s to save this picture or others to exit.\n"

        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)

        if key == ord('s'):
            cv2.imwrite(name, img)

        cv2.destroyAllWindows()

    def Roberts(self):
        self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        #  pprint(self.img)
        #  print type(self.img), len(self.img), len(self.img[0])
        m1 = np.array([[-1, 0], [0, 1]])
        m2 = np.array([[0, -1], [1, 0]])
        
        self.img1 = np.zeros(self.img.shape, np.uint8)
        self.img2 = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 1):
            for y in xrange(self.W - 1):
                #  if x + 1 == 375:
                    #  pdb.set_trace()
                mat = np.array([[self.img[x, y], self.img[x, y + 1]], [self.img[x + 1, y], self.img[x + 1, y + 1]]])
                #  pprint(mat)
                res1 = abs(np.sum(mat * m1))
                res2 = abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)

        self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.showImage("Roberts.jpg", self.out)
        self.sharpen = self.out + self.img
        self.showImage("Roberts_Sharpen.jpg", self.sharpen)

    def Prewitt(self):
        self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        #  pprint(self.img)
        #  print type(self.img), len(self.img), len(self.img[0])
        m1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        m2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        
        self.img1 = np.zeros(self.img.shape, np.uint8)
        self.img2 = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                #  if x + 1 == 375:
                    #  pdb.set_trace()
                mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                #  pprint(mat)
                res1 = abs(np.sum(mat * m1))
                res2 = abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)

        self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.showImage("Prewitt.jpg", self.out)
        self.sharpen = self.out + self.img
        self.showImage("Prewitt_Sharpen.jpg", self.sharpen)

    def Sobel(self):
        self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        #  pprint(self.img)
        #  print type(self.img), len(self.img), len(self.img[0])
        m1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        m2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        
        self.img1 = np.zeros(self.img.shape, np.uint8)
        self.img2 = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                #  if x + 1 == 375:
                    #  pdb.set_trace()
                mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                #  pprint(mat)
                res1 = abs(np.sum(mat * m1))
                res2 = abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)

        self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.showImage("Sobel.jpg", self.out)
        self.sharpen = self.out + self.img
        self.showImage("Sobel_Sharpen.jpg", self.sharpen)

    def lapacian(self):
        self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        #  pprint(self.img)
        #  print type(self.img), len(self.img), len(self.img[0])
        m1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        m2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        m3 = np.array([[0, -1, 0], [-1, 4, 1], [0, -1, 0]])
        m4 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        
        self.img1 = np.zeros(self.img.shape, np.uint8)
        self.img2 = np.zeros(self.img.shape, np.uint8)
        self.img3 = np.zeros(self.img.shape, np.uint8)
        self.img4 = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                #  if x + 1 == 375:
                    #  pdb.set_trace()
                mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                #  pprint(mat)
                res1 = abs(np.sum(mat * m1))
                res2 = abs(np.sum(mat * m2))
                res3 = abs(np.sum(mat * m3))
                res4 = abs(np.sum(mat * m4))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                self.img3[x, y] = res3
                self.img4[x, y] = res4
                #  pprint(res1)
                #  pprint(res2)

        self.out = self.img1 + self.img2 + self.img3 + self.img4
        #  pprint(self.out)
        self.showImage("lapacian.jpg", self.out)
        self.sharpen = self.out + self.img
        self.showImage("Lapcian_Sharpen.jpg", self.sharpen)

if __name__ == "__main__":
    img = Image("./test.jpg")
    #  img.Roberts()
    #  img.Prewitt()
    #  img.Sobel()
    img.lapacian()

