#coding=utf-8
__Auther__ = "M4x"

import numpy as np
import cv2
import pdb

class Video(object):
	def __init__(self, file, method):
		print "Only *.avi is supported"
		self.method = method # 0:  Subtracting successive frames; 1: Subtracting histograms
		self.st = 0
		self.flag = False
		self.video = cv2.VideoCapture(file)
		# if self.video.isOpened():
			# print self.video.read()
		# else:
		if not self.video.isOpened():
			print "BAD VIDEO FORMAT! Only *.avi is supported!"

	def subImages(self, img1, img2):
		# in case of InterOverflow
		img1 = img1.astype(np.int)
		img2 = img2.astype(np.int)
		sub = abs(img1 - img2).astype(np.uint8)
		return sub

	def showImage(self, img):
		print "%d changed images found. Press s to save or others to exit." % (self.st + 1)
		cv2.imshow(str(self.st) + ".jpg", img)
		if cv2.waitKey(0) & 0xff == ord('s'):
			cv2.imwrite(str(self.st) + ".jpg", img)
			
		cv2.destroyAllWindows()
		
	def getChange(self):
		_, lastFrame = self.video.read()
		while self.video.isOpened():
			notLast, frame = self.video.read()
			# print frame.size
			
			if not notLast:
				if not self.flag:
					print "The whole video is in the same camera lens."
					cv2.destroyAllWindows()
					self.video.release()
				
				else:
					print "%d different camera lens found all toghther." % self.st
				break
			
			#Subtracting successive frames
			elif self.method == 0: 
				if np.sum(self.subImages(lastFrame, frame)) / frame.size > 10:
					self.flag = True
					self.showImage(frame)
					self.st += 1
			
			#Subtracting histograms
			elif self.method == 1:
				if np.sum(self.subImages(self.convertToGray(lastFrame), self.convertToGray(frame))) / frame.size > 2:
					self.flag = True
					self.showImage(frame)
					self.st += 1
			
			lastFrame = frame
			
	def convertToGray(self, img):
		#convert RGB to GRAY
		return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
		
	
			
# video = Video('test1.avi', 0) # Subtracting successive frames
# video.getChange()
# video = Video('test2.avi', 0)
# video.getChange()
# video = Video('test1.avi', 1) # Subtracting histograms
# video.getChange()
video = Video('test2.avi', 1)
video.getChange()
