#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from time import sleep
from math import radians, cos, sin, fabs
import numpy as np
import cv2
import pdb

class Picture(object):
    def __init__(self, file):
        self.img = cv2.imread(file)
        self.H, self.W, self._ = self.img.shape
        print "At first, the original image."
        self.show_img("Original_Image.jpg", self.img)

    def show_img(self, name, img):
        print "Press s to save this picture or others to exit.\n"
        #  sleep(0.5)

        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)

        if key == ord('s'):
            cv2.imwrite(name, img)

        cv2.destroyAllWindows()

    def Translation(self, delta_x, delta_y):
        #  res1 = self.img.copy()
        res1 = np.zeros(self.img.shape, np.uint8)
        #  res2 = self.img.copy()
        res2 = np.zeros(self.img.shape, np.uint8)
        #  res3 = self.img.copy()
        res3 = np.zeros(self.img.shape, np.uint8)

        #From result to original
        for i in xrange(self.H):
            for j in xrange(self.W):
                #fill the rest with original image
                res1[i, j] = self.img[(i - delta_x) % self.W, (j - delta_y) % self.H]
                if i >= delta_x and j >= delta_y:
                    res2[i, j] = self.img[i - delta_x, j - delta_y]
                    res3[i, j] = self.img[i - delta_x, j - delta_y]
                else:
                    res2[i, j] = (0x0, 0x0, 0x0)#fill the blank with black point
                    res3[i, j] = (0xff, 0xff, 0xff)#fill the blank with white point

        print "Next is the translated image."
        self.show_img("Translation_Image_original.jpg", res1)
        self.show_img("Translation_Image_black.jpg", res2)
        self.show_img("Translation_Image_white.jpg", res3)
                
    #  def Resize(self, nx, ny):




    def Rotation(self, deg):
        #  res1 = self.img.copy()
        res1 = np.zeros(self.img.shape, np.uint8)
        #  res2 = self.img.copy()
        res2 = np.zeros(self.img.shape, np.uint8)

        deg = radians(deg)#Convert redians to degrees
        C = cos(deg)
        S = sin(deg)
        A = -0.5 * self.W * C + 0.5 * self.H * S + 0.5 * self.W
        B = -0.5 * self.W * S - 0.5 * self.H * C + 0.5 * self.H

        #x1 = x0 * cos(a) - y0 * sin(a) - 0.5Ncos(a) + 0.5Msin(a) + 0.5N
        #y1 = x0 * sin(a) + y0 * cos(a) - 0.5Nsin(a) - 0.5Mcos(a) + 0.5M 
        #x0 = (Cx - AC + Sy - BS) / (CC + CS)
        #y0 = (Cy - BC - Sx + AS) / (SS + CC)

        trans_x = lambda x, y: (C * x - A * C + S * y - B * S) / (C * C + C * S)
        trans_y = lambda x, y: (C * y - B * C - S * x + A * S) / (S * S + C * C)

        for x in xrange(self.W):
            for y in xrange(self.H):
                tx = int(trans_x(x, y))
                ty = int(trans_y(x, y))
                #  print trans_x(x, y), type(trans_x(x, y))
                #  print trans_y(x, y), type(trans_y(x, y))
                if 0 < tx < self.W and 0 < ty < self.H:
                    res1[x, y] = self.img[tx, ty]
                    res2[x, y] = self.img[tx, ty]
                else:
                    res1[x, y] = (0x0, 0x0, 0x0)#fill the blank with black point
                    res2[x, y] = (0xff, 0xff, 0xff)#fill the blank with white point

        print "Next is the rotated image."
        self.show_img("Rotation_Image_black.jpg", res1)
        self.show_img("Rotation_Image_white.jpg", res2)

img = Picture("./test.jpg")
img.Translation(10, 40)
img.Rotation(45)
