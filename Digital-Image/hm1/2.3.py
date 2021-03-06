#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from math import radians, cos, sin, fabs
import numpy as np
import cv2
import pdb

class Picture(object):
    def __init__(self, file):
        self.img = cv2.imread(file)
        #  print self.img.shape
        self.H, self.W, self.CH = self.img.shape
        print "At first, the original image."
        self.show_img("Original_Image.jpg", self.img)

    def show_img(self, name, img):
        print "Press s to save this picture or others to exit.\n"

        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)

        if key == ord('s'):
            cv2.imwrite(name, img)

        cv2.destroyAllWindows()

    def Translation(self, delta_x, delta_y):
        res1 = np.zeros(self.img.shape, np.uint8)
        res2 = np.zeros(self.img.shape, np.uint8)
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
                
    def Resize(self, nx, ny):
        if 0 < nx <= 1 and 0 < ny <= 1:
            rw = int(self.W * ny)
            rh = int(self.H * nx)
            #  print rh, rw

            res1 = np.zeros((rh, rw, self.CH), np.uint8)
            res2 = np.zeros((rh, rw, self.CH), np.uint8)
            #  print res.shape
            for y in xrange(rh):
                for x in xrange(rw):
                    res1[y, x] = self.img[int(y / nx), int(x / ny)]

                    #  fill every point with the average of the matrix
                    y1 = int(y / nx)
                    y2 = int((y + 1) / nx)
                    x1 = int(x / ny)
                    x2 = int((x + 1) / ny)
    
                    ave = [0x0, 0x0, 0x0]
                    for j in xrange(y1, y2):
                        for i in xrange(x1, x2):
                            for k in xrange(3):
                                ave[k] += self.img[j, i][k]
    
                    num = (x2 - x1) * (y2 - y1)
                    for k in xrange(3):
                        ave[k] /= num
    
                    res2[y, x] = ave

            print "Next is the shrinked image."
            self.show_img("Shrinked_Image.jpg", res1)
            self.show_img("Better_Shrinked_Image.jpg", res2)

        elif nx > 1 and ny > 1:
            rw = int(self.W * ny - ny)
            rh = int(self.H * nx - nx)

            res1 = np.zeros((rh, rw, self.CH), np.uint8)
            res2 = np.zeros((rh, rw, self.CH), np.uint8)
            #  print res.shape
            for i in xrange(rh):
                for j in xrange(rw):
                    res1[i, j] = self.img[int(i / nx), int(j / ny)]

                    #The following will cost a long time
                    x1 = int((i + 1) / nx - 1)
                    y1 = int((j + 1) / ny - 1)
                    p = float(i) / nx - x1
                    q = float(j) / ny - y1

                    ave = [0x0, 0x0, 0x0]
                    for k in xrange(3):
                        ave[k] = int(self.img[x1, y1][k] * (1 - q) * (1 - p) + self.img[x1 + 1, y1][k] * p * (1 - q) + self.img[x1, y1 + 1][k] * (1 - p) * q + self.img[x1 + 1, y1 + 1][k] * p * q)

                    res2[i, j] = ave
            
            else:
                print "Error resize paremeters!"

            print "Next is the zoomed image."
            self.show_img("Zoomed_Image.jpg", res1)
            self.show_img("Better_Zoomed_Image.jpg", res2)


    def Rotation(self, deg):
        deg = radians(deg)#Convert redians to degrees
        C = cos(deg)
        S = sin(deg)

        X1 = int(fabs(0.5 * self.H * C + 0.5 * self.W * S))
        X2 = int(fabs(0.5 * self.H * C - 0.5 * self.W * S))
        Y1 = int(fabs(-0.5 * self.H * S + 0.5 * self.W * C))
        Y2 = int(fabs(-0.5 * self.H * S - 0.5 * self.W * C))
        H = int(2 * max(Y1,Y2))
        W = int(2 * max(X1,X2))

        A = -0.5 * self.W * C + 0.5 * self.H * S + 0.5 * W
        B = -0.5 * self.W * S - 0.5 * self.H * C + 0.5 * H

        size = (H, W, self.CH)
        res1 = np.zeros(size, np.uint8)
        res2 = np.zeros(size, np.uint8)

        #x1 = x0 * C - y0 * S - 0.5NC + 0.5MS + 0.5N'
        #y1 = x0 * S + y0 * C - 0.5NS - 0.5MC + 0.5M' 
        #x0 = (Cx - AC + Sy - BS) / (CC + CS)
        #y0 = (Cy - BC - Sx + AS) / (SS + CC)

        trans_x = lambda x, y: (C * x - A * C + S * y - B * S) / (C * C + C * S)
        trans_y = lambda x, y: (C * y - B * C - S * x + A * S) / (S * S + C * C)

        for x in xrange(W):
            for y in xrange(H):
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
        self.show_img("Rotation_Image_Black.jpg", res1)
        self.show_img("Rotation_Image_White.jpg", res2) 

    def Deviation(self, nx, ny):
        dw = int(self.H * float(nx) + self.W)
        dh = int(self.W + float(ny) * self.H)
        res1 = np.zeros((dh, dw, self.CH), np.uint8)
        res2 = np.zeros((dh, dw, self.CH), np.uint8)
        #  print res.shape

        for y in xrange(dh):
            for x in xrange(dw):
                ox = int(x - nx * y)
                oy = int(y - ny * x)
                if 0 <= ox < self.W and 0 <= oy < self.H:
                    res1[y, x] = self.img[oy, ox]
                    res2[y, x] = self.img[oy, ox]
                else:
                    res1[y, x] = (0x0, 0x0, 0x0)#black point
                    res2[y, x] = (0xff, 0xff, 0xff)#white point

        print "Next is the deviated image."
        self.show_img("Deviated_Image_Black.jpg", res1)
        self.show_img("Deviated_Image_White.jpg", res2)


if __name__ == "__main__":
    img = Picture("./test.jpg")
    #  img.Translation(50, 70)
    #  img.Resize(0.5, 0.7)
    #  img.Resize(1.5, 1.7)
    #  img.Rotation(45)
    img.Deviation(0, 0.5)
    img.Deviation(0.5, 0)
    img.Deviation(0.5, 0.5)
