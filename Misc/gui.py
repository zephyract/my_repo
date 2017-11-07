#coding = utf-8
__Auther__ = "M4x"

'''
This programm is developed by py3.5 for my girlfriend, which works as 
a timer and is able to record every answer from users.
'''

from tkinter import *
from time import sleep, clock
from random import shuffle
from os import remove
import pdb

class Question(Frame):
	def __init__(self, i, ques, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.i = i
		self.ques = ques
		self.show_question()

	def show_question(self):
		self.qlb = Label(self, text = str(self.i) + " " + self.ques, font = ("Helvetica", 18))
		self.qlb.pack(side = "left")
		self.st = clock()
		self.btn1 = Button(self, text = u"是", command = self.yes)
		self.btn1.pack(side = "left")
		self.btn2 = Button(self, text = u"否", command = self.no)
		self.btn2.pack(side = "left")
		# sleep(3)
		# self.qlb.pack_forget()
		# self.btn1.pack_forget()
		# self.btn2.pack_forget()

	def yes(self):
		cost = clock() - self.st
		with open("answer.txt", "a") as f:
			f.write(str(self.i) + ". " + self.ques + " " + u"是" + " %.2f" % cost + "\n")

	def no(self):
		cost = clock() - self.st
		with open("answer.txt", "a") as f:
			f.write(str(self.i) + ". " + self.ques + " " + u"否" + " %.2f" % cost + "\n")

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		# pdb.set_trace()
		self.get_questions()

		self.random_ques()

	def get_questions(self):
		self.ques1 = [u"进入实验室时，你推开了抵着门的%s吗？" % i
		        for i in [u"一个暖瓶", u"一个花盆", u"一个茶几",
		                  u"一把椅子", u"一个纸盒",
		                  u"一张桌子"]]

		self.ques2 = [u"离开实验室时，你拿走了%s吗？" % i
			    for i in [u"钥匙", u"手机", u"光盘",
			              u"钱包", u"手表",
			              u"饭卡"]]

		self.ques3 = [u"你在翻东西时，听到了%s的声音吗？" % i
			    for i in [u"敲门", u"闹钟", u"吵架",
			              u"说话", u"贺卡",
			              u"手机"]]


	def random_ques(self):
		shuffle(self.ques1)
		shuffle(self.ques2)
		shuffle(self.ques3)

		for i, j in enumerate(self.ques1):
			ques = Question(i, j, self)
			ques.show_question()
			# sleep(3)
		for i, j in enumerate(self.ques2):
			ques = Question(i, j, self)
			ques.show_question()
			# sleep(3)
		for i, j in enumerate(self.ques3):
			ques = Question(i, j, self)
			ques.show_question()
			# sleep(3)
def run():
	try:
		remove("answer.txt")
	except:
		pass

	app = Application()
	app.master.title("TEST TITLE")
	app.master.minsize(600, 300)
	app.mainloop()


if __name__ == "__main__":
	run()
