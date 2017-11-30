#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import cv2
import numpy as np
from pprint import pprint
import pdb

class Image(object):
    def __init__(self, file):
        self.img = cv2.imread(file, 0)#read as gray image
        self.H, self.W = self.img.shape
        self.showImage("Original.jpeg", self.img)

    def showImage(self, name, img):
        print "Press s to save this picture or others to exit.\n" 
        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)

        if key == ord('s'):
            cv2.imwrite(name, img)

    def fft(self, img):
        return np.fft.fftshift(np.fft.fft2(img))

    def ifft(self, img):
        return np.fft.ifft2(np.fft.ifftshift(img))

    def highPass(self):
        mask = np.ones(self.img.shape)
        mask[self.H / 2 - 30: self.H / 2 + 30, self.W / 2 - 30: self.W / 2 + 30] = 0
        pprint(mask)
        return mask

    def lowPass(self):
        mask = np.ones(self.img.shape)
        mask[self.H / 2 - 30: self.H / 2 + 30, self.W / 2 - 30: self.W / 2 + 30] = 0
        #  pprint(mask)
        mask = 1 - mask
        return mask

    def gaussLowPass(self, D):
        center = (self.H // 2, self.W // 2)
        mask = np.empty(self.img.shape)
        for u in xrange(self.H):
            for v in xrange(self.W):
                #  pdb.set_trace()
                duv = np.sqrt(pow((u - center[0]), 2) + pow((v - center[1]), 2))
                mask[u][v] = pow(np.e, -(pow(duv, 2) / pow(D, 2)))

        #  pprint(mask)
        return mask

    def gaussHighPass(self, D):
        center = (self.H // 2, self.W // 2)
        mask = np.empty(self.img.shape)
        for u in xrange(self.H):
            for v in xrange(self.W):
                duv = np.sqrt(pow((u - center[0]), 2) + pow((v - center[1]), 2))
                mask[u][v] = 1 - pow(np.e, -(pow(duv, 2) / pow(D, 2)))

        #  pprint(mask)
        return mask


    def butterWorth(self, D, n):
        center = (self.H // 2, self.W // 2)
        mask = np.empty(self.img.shape)
        for u in xrange(self.H):
            for v in xrange(self.W):
                duv = np.sqrt(pow((u - center[0]), 2) + pow((v - center[1]), 2))
                mask[u][v] = 1 / pow((1 + (duv / D)), 2 * n)

        #  pprint(mask)
        return mask

    def frequencyFilter(self, method, D = 0.5, n = 1):
        #  pdb.set_trace()
        if method.lower() == "highpass":
            mask = self.highPass()
        elif method.lower() == "lowpass":
            mask = self.highPass()
        elif method.lower() == "butterworth":
            mask = self.butterWorth(D, n)
        elif method.lower() == "gausslowpass":
            mask = self.gaussLowPass(100)
        elif method.lower() == "gausshighpass":
            mask = self.gaussHighPass(100)
        else:
            print "[!]method error!"
            exit(0)

        out = self.fft(self.img) * mask
        res = self.ifft(out)
        res = np.abs(res)
        res = (res - np.amin(res)) / (np.amax(res) - np.amin(res))

        if method.lower() == "highpass":
            self.showImage("HighPass_filter.jpeg", res)
        elif method.lower() == "lowpass":
            self.showImage("LowPass_filter.jpeg", res)
        elif method.lower() == "butterworth":
            self.showImage("butterWorth.jpeg", res)
        elif method.lower() == "gausslowpass":
            self.showImage("GaussLowPass.jpeg", res)
        elif method.lower() == "gausshighpass":
            self.showImage("gaussHighPass.jpeg", res)

    def spaceFilter(self):
        mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        res = np.zeros(self.img.shape, np.uint8)

        for x in xrange(self.H - 2):
            for y in xrange(self.W - 2):
                mat = self.img[x: x + 3, y: y + 3]
                res[x, y] = np.abs(np.sum(mat * mask / 16))

        self.showImage("spaceFilter.jpeg", res)

if __name__ == "__main__":
    img = Image("./messi.jpeg")
    #  img.frequencyFilter("highpass")
    #  img.frequencyFilter("lowpass")
    #  img.frequencyFilter("gaussLowPass", 100)
    #  img.frequencyFilter("gaussHighPass", 50)
    #  img.frequencyFilter("butterWorth", 100, 2)
    img.spaceFilter()
