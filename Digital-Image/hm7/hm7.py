#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from copy import deepcopy as cp
import skimage.morphology as sm

class MorphologyDealing(object):
    def __init__(self):
        self.kernel3 = np.ones((3, 3), np.uint8)
        self.kernel5 = np.ones((5, 5), np.uint8)
        self.kernel9 = np.ones((9, 9), np.uint8)
        self.kernel15 = np.ones((15, 15), np.uint8)
        self.kernel25 = np.ones((25, 25), np.uint8)

    def show(self, key1, key2, key3, pivot):
        plt.figure(key1)
        plt.subplot(1, 2, 1)
        plt.imshow(img, 'gray')
        plt.title(key2)
        plt.subplot(1, 2, 2)
        plt.title(key3)
        plt.imshow(pivot, 'gray')

    def erosionImg(self, img):
        erosion = cv2.erode(img, self.kernel5, 1)
        self.show('erosion', 'original', 'erosion', erosion)
        return cp(erosion)
        
    def dilateImg(self, img):
        diatex = cv2.dilate(img, self.kernel5, 1)
        self.show("dilate", "original", "diatex", diatex)
        return cp(diatex)
        
    def ExopenImg(self, img):
        moropen = cv2.morphologyEx(img, cv2.MORPH_OPEN, self.kernel15)
        self.show("open op", "original", "MORPH_OPEN", moropen)
        return cp(moropen)
        
    def ExcloseImg(self, img):
        morclose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, self.kernel15)
        self.show("close op", "original", "MORPH_CLOSE", morclose) 
        return cp(morclose)
        
    def Skeletionize(self, img):
        sk_img = sm.skeletonize(img)
        self.show("get skeletonize", "original", "skeletonize", sk_img)
        return cp(sk_img)
        
    def Hull(self, img):
        hull_img = sm.convex_hull_image(img)
        self.show("get convex hull", "original", "convex_hull_image", hull_img)
        return cp(hull_img)
        
    def Labeled(self, img):
        label_img = sm.label(img, neighbors=8)
        self.show("get labels", "original", "labeled_image", label_img)
        return cp(label_img)
        
    def Thin(self, img):
        thin_img = sm.thin(img, max_iter=None)
        self.show("get thin", "original", "thin_image", thin_img)
        return cp(thin_img)
        
    def Thick(self, img):
        w, h = img.shape
        for i in xrange(w):
            for j in xrange(h):
                img[i, j] = 1 - img[i, j]
        thick_img = sm.thin(img, max_iter=None)
        for i in xrange(w):
            for j in xrange(h):
                thick_img[i, j] = not thick_img[i, j]
        self.show("get thick", "original", "thin_image", thick_img)
        return cp(thick_img)
        
    def Skin(self, img):
        result = self.erosionImg(img)
        result = self.ExopenImg(result)
        result = self.dilateImg(result)
        plt.figure()
        plt.imshow(result, 'gray')
        return cp(result)

    def binaryGet(self, img, threshold):
        ret, binary_img = cv2.threshold(img, threshold, 1, cv2.THRESH_BINARY)
        return cp(binary_img)
        
if __name__ == '__main__':
    md = MorphologyDealing()
    img = cv2.imread('./Steve-Jobs.jpg', 0)
    img = md.binaryGet(img, 127)
    #  res=md.erosionImg(img)
    #  plt.figure()
    #  plt.imshow(res,'gray')
    md.dilateImg(img)
    md.ExopenImg(img)
    md.ExcloseImg(img)
    md.Hull(img)
    md.Skeletionize(img)
    md.Labeled(img)
    md.Thin(img)
    md.Thick(img)
    md.Skin(img)
    plt.show()
