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
        # 选择5*5的正方形进行膨胀操作 
        diatex = cv2.dilate(img, self.kernel5, 1)
        # 结果显示
        self.show("dilate", "original", "diatex", diatex)
        return cp(diatex)
        
    def morphologyExopen_img(self, img):
        # 选择5*5的正方形进行开运算
        moropen = cv2.morphologyEx(img, cv2.MORPH_OPEN, self.kernel15)
        # 结果显示
        self.show("open op", "original", "MORPH_OPEN", moropen)
        return cp(moropen)
        
    def morphologyExclose_img(self, img):
        # 选择5*5的正方形进行闭运算
        morclose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, self.kernel15)
        # 结果显示
        self.show("close op", "original", "MORPH_CLOSE", morclose) 
        return cp(morclose)
        
    def morphologySkeletonize(self, img):
        # 实施骨架提取算法
        sk_img = sm.skeletonize(img)
        self.show("get skeletonize", "original", "skeletonize", sk_img)
        # 结果显示
        return cp(sk_img)
        
    def morphologyHull(self, img):
        # 凸壳
        hull_img = sm.convex_hull_image(img)
        self.show("get convex hull", "original", "convex_hull_image", hull_img)
        return cp(hull_img)
        
    def morphologyLabeled(self, img):
        # 连通分量提取
        label_img = sm.label(img, neighbors=8)
        self.show("get labels", "original", "labeled_image", label_img)
        return cp(label_img)
        
    def morphologyThin(self, img):
        # 细化操作
        thin_img = sm.thin(img, max_iter=None)
        # max_iter optional regardless if ther value of this parameter
        self.show("get thin", "original", "thin_image", thin_img)
        return cp(thin_img)
        
    def morphologyThick(self, img):
        # 粗化操作
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
        
    def getSkin(self, img):
        result = self.erosionImg(img)
        result = self.morphologyExopen_img(result)
        result = self.dilateImg(result)
        plt.figure()
        plt.imshow(result, 'gray')
        return cp(result)

    def binary_get(self, img, threshold):
        ret, binary_img = cv2.threshold(img, threshold, 1, cv2.THRESH_BINARY)
        return cp(binary_img)
        
if __name__ == '__main__':
    md = MorphologyDealing()
    img = cv2.imread('./Steve-Jobs.jpg', 0)
    img = md.binary_get(img, 127)
    #  res=md.erosionImg(img)
    #  plt.figure()
    #  plt.imshow(res,'gray')
    md.dilateImg(img)
    md.morphologyExopen_img(img)
    md.morphologyExclose_img(img)
    md.morphologyHull(img)
    md.morphologySkeletonize(img)
    md.morphologyLabeled(img)
    md.morphologyThin(img)
    md.morphologyThick(img)
    md.getSkin(img)
    plt.show()
