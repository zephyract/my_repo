#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import numpy as np
import cv2
import os

class Image(object):
    def __init__(self, file):
        self.img = cv2.imread(file)
        self.W, self.H, _ = self.img.shape
        self.showImage("original.png", self.img)

    def showImage(self, name, img):
        cv2.imshow(name, img)
        key = (cv2.waitKey(0) & 0xff)
        if key == ord('s'):
            cv2.imwrite(name, img)
            
    def convert(self, contrast, bright):
        '''
        调整亮度和对比度
        contrast, bright均为放大倍数
        '''
        mean = np.mean(self.img)
        out = self.img - mean
        out = out * contrast + mean * bright
        out = out / 255
        self.showImage("converted.png", out)

    def pencile(self, sigma_s = 50, sigma_r = 0.15, shade_factor = 0.04):
        '''
        制作铅笔画
        sigma_s: 滑动窗口大小(0 ~ 200)
        sigma_r: 颜色不相似度(0 ~ 1.0, 不相似度越大代表滤波后颜色相似区域越大)
        shade_factor: 光照因子(0 ~ 0.1), 控制图像亮度, 越大越亮
        '''
        outGray, outColor = cv2.pencilSketch(self.img, sigma_s = sigma_s, sigma_r = sigma_r, shade_factor = shade_factor)
        self.showImage("pencileGray.png", outGray)
        self.showImage("pencileColor.png", outColor)

    def stylize(self, sigma_s = 50, sigma_r = 0.15):
        '''
        制作风格化图像
        参数与pencil类似
        '''
        out = cv2.stylization(self.img, sigma_s = sigma_s, sigma_r = sigma_r)
        self.showImage("stylization.png", out)

    def detailEnhance(self, sigma_s = 50, sigma_r = 0.15):
        '''
        细节增强
        参数同上
        '''
        out = cv2.detailEnhance(self.img, sigma_s = 50, sigma_r = sigma_r)
        self.showImage("detailEnhance.png", out)

    def edgePreserve(self, flags = 1, sigma_s = 50, sigma_r = 0.15):
        '''
        flags: 边缘保持方法(迭代比归一化快), 1 -> 迭代滤波, 2 -> 归一化
        '''
        out = cv2.edgePreservingFilter(self.img, flags = 1, sigma_s = 50, sigma_r = 0.15)
        self.showImage("edgePreservingFilter.png", out)

if __name__ == "__main__":
    img = Image("./test.png")
    #  img.convert(1.5, 0.7)
    #  img.pencile()
    #  img.stylize()
    #  img.detailEnhance()
    #  img.edgePreserve()
