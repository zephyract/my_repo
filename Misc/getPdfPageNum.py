# -*- coding: utf-8 -*-
__Auther__ = "M4x"

from pyPdf import PdfFileReader
from os import listdir

def getNum(files):
	pages = []
	for f in files:
		pdf = PdfFileReader(file(f, "rb"))
		print f, pdf.getNumPages()
		pages.append(pdf.getNumPages())

	print sum(pages), "all together"

def getName():
	pdfs = [i for i in listdir(".") if i.endswith(".pdf")]
	return pdfs

if __name__ == '__main__':
	getNum(sorted(getName()))