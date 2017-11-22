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
                #  mat = np.array([[self.img[x, y], self.img[x, y + 1]], [self.img[x + 1, y], self.img[x + 1, y + 1]]])
                mat = self.img[x: x + 2, y : y+2]
                #  pprint(mat)
                res1 = np.abs(np.sum(mat * m1))
                res2 = np.abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)

        self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.showImage("Roberts.jpg", self.out.astype(np.uint8))
        #  self.sharpen = self.out + self.img
        #  self.showImage("Roberts_Sharpen.jpg", self.sharpen)

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
                #  mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                mat = self.img[x: x + 3, y: y + 3]
                #  pprint(mat)
                res1 = np.abs(np.sum(mat * m1))
                res2 = np.abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)

        #  self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.showImage("Prewitt1.jpg", self.img1.astype(np.uint8))
        #  self.sharpen = self.out + self.img
        self.showImage("Prewitt2.jpg", self.img2.astype(np.uint8))

    def Sobel(self, img = None):
        #  pdb.set_trace()
        if img is None:
            self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        else:
            self.img = img
        #  pprint(self.img)
        #  print type(self.img), len(self.img), len(self.img[0])
        m1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])#"horizontal"
        m2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])#"vertical"
        
        self.img1 = np.zeros(self.img.shape, np.uint8)
        self.img2 = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                #  if x + 1 == 375:
                    #  pdb.set_trace()
                #  mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                mat = self.img[x: x + 3, y: y + 3]
                #  pprint(mat)
                res1 = np.abs(np.sum(mat * m1))
                res2 = np.abs(np.sum(mat * m2))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                #  pprint(res1)
                #  pprint(res2)
        #  self.out = self.img1 + self.img2
        #  pprint(self.out)
        self.img1 = self.img1 * (255 / np.max(self.img))
        self.img2 = self.img2 * (255 / np.max(self.img))
        if img is None:
            self.showImage("Sobel1.jpg", self.img1.astype(np.uint8))
            #  self.sharpen = self.out + self.img
            self.showImage("Sobel2.jpg", self.img2.astype(np.uint8))
        return self.img1.astype(np.uint8), self.img2.astype(np.uint8)

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
                #  mat = np.array([[self.img[x, y], self.img[x, y + 1], self.img[x, y + 2]], [self.img[x + 1, y], self.img[x + 1, y + 1], self.img[x + 1, y + 2]], [self.img[x + 2, y], self.img[x + 2, y + 1], self.img[x + 2, y + 2]]])
                mat = self.img[x: x + 3, y: y + 3]
                #  pprint(mat)
                res1 = np.abs(np.sum(mat * m1))
                res2 = np.abs(np.sum(mat * m2))
                res3 = np.abs(np.sum(mat * m3))
                res4 = np.abs(np.sum(mat * m4))
                self.img1[x, y] = res1
                self.img2[x, y] = res2
                self.img3[x, y] = res3
                self.img4[x, y] = res4
                #  pprint(res1)
                #  pprint(res2)

        #  self.out = self.img1 + self.img2 + self.img3 + self.img4
        #  pprint(self.out)
        self.showImage("lapacian1.jpg", self.img1.astype(np.uint8))
        #  self.sharpen = self.out + self.img
        self.showImage("lapacian2.jpg", self.img2.astype(np.uint8))
        self.showImage("lapacian3.jpg", self.img3.astype(np.uint8))
        self.showImage("lapacian4.jpg", self.img4.astype(np.uint8))


    def GaussianBlur(self):
        self.img = cv2.cvtColor(self.oriImg, cv2.COLOR_RGB2GRAY)
        #  self.showImage("Grey.jpg", self.img)
        self.out = np.zeros(self.img.shape, np.uint8)
        m = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                mat = self.img[x: x + 3, y: y + 3]
                #  pdb.set_trace()
                #  try:
                    #  res = np.abs(np.sum(m * mat / 16))
                #  except:
                    #  pdb.set_trace()
                res = np.abs(np.sum(m * mat / 16))
                self.out[x, y] = res

        #  self.showImage("GaussianBlur.jpg", self.out.astype(np.uint8))
        return self.out.astype(np.uint8)
                
    def DFS(self, step, st):
        dxy = [(0, 1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, -1), (-1, -1)]
        route = [st]
        while route:
            now = route.pop()
            if self.visited[now] == 1:
                break

            self.visited[now] = 1
            for d in dxy:
                nt = (now[0] + d[0], now[1] + d[1])
                if not self.visited[nt] and self.nms[nt] > self.min and nt[0] < self.H - 1 and nt[0] >= 0 and nt[1] < self.W - 1 and nt[1] >= 0:
                    route.append(nt)


    def canny(self, MIN, MAX):
        #  pdb.set_trace()
        self.img = self.GaussianBlur()
        Gx, Gy = self.Sobel(self.img)

        self.G = np.sqrt(np.square(Gx.astype(np.float64)) + np.square(Gy.astype(np.float64)))
        self.deg = np.arctan2(Gy.astype(np.float64), Gx.astype(np.float64))
        #  self.showImage("canny.jpg", self.G)

        self.m = np.zeros(self.deg.shape, np.uint8)
        for i in xrange(1, self.H - 1):
            for j in xrange(1, self.W - 1):
                if [self.deg[i][j]] * 2 > [self.deg[i - 1][j], self.deg[i + 1][j]]:
                    self.m[i - 1][j - 1] = 1
                elif [self.deg[i][j]] * 2 > [self.deg[i][j + 1], self.deg[i][j - 1]]:
                    self.m[i - 1][j - 1] = 1
                elif [self.deg[i][j]] * 2 > [self.deg[i - 1][j], self.deg[i][j + 1]]:
                    self.m[i - 1][j - 1] = 1
                else:
                    self.m[i - 1][j - 1] = 0

        self.nms = (self.m * (255 / np.max(self.deg))).astype(np.uint8)
        #  self.showImage("canny,jpg", self.out)
        self.min = np.max(self.nms) / (MIN + MAX) * MAX
        self.max = np.max(self.nms) / (MIN + MAX) * MIN

        self.visited = np.zeros(self.nms.shape, np.uint8)
        selectList = []
        for i in xrange(self.H):
            for j in xrange(self.W):
                if self.nms[i, j] > self.max:
                    selectList.append((i, j))

        for p in selectList:
            self.DFS(self.nms, p)

        self.out = self.nms * self.visited
        self.showImage("canny.jpg", self.out)

if __name__ == "__main__":
    img = Image("./test.jpg")
    img.Roberts()
    img.Prewitt()
    img.Sobel()
    img.lapacian()
    #  img.GaussianBlur()
    img.canny(1, 3)
