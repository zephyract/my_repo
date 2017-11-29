#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import cv2
import numpy as np
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
        mask = np.ones(self.img.shape, np.uint8)
        mask[self.H / 2 - 30: self.H / 2 + 30, self.W / 2 - 30: self.W / 2 + 30] = 0
        return mask

    def lowPass(self):
        mask = np.zeros(self.img.shape, np.uint8).astype(float64)
        mask[self.H / 2 - 30: self.H / 2 + 30, self.W / 2 - 30: self.W / 2 + 30] = 1

    def butterWorth(self, D, n):
        INF = 0xffffff
        mask = np.ones(self.img.shape, np.uint8)
        r = lambda x, y: np.sqrt(pow(x - self.W / 2, 2) + pow(y - self.H / 2, 2))
        for x in xrange(self.H):
            for y in xrange(self.W):
                #  pdb.set_trace()
                t = r(x, y) / (D * D)
                mask[x, y] = INF / (pow(t, n) + 1)

        #  pdb.set_trace()
        print mask.astype(np.uint8)
        return mask.astype(np.uint8)

    def frequencyFilter(self, method, D = 0.5, n = 1):
        #  pdb.set_trace()
        if method.lower() == "highpass":
            mask = self.highPass()
        elif method.lower() == "lowpass":
            mask = self.highPass()
        elif method.lower() == "butterworth":
            mask = self.butterWorth(D, n)

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


if __name__ == "__main__":
    img = Image("./messi.jpeg")
    #  img.frequencyFilter("highpass")
    #  img.frequencyFilter("lowpass")
    img.frequencyFilter("butterWorth", 0.5, 1)
