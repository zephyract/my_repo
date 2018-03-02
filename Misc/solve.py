#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from PIL import Image
from PIL.ImageOps import invert
import re

with open("./xy") as f:
    s = f.read().decode("hex").strip("\n").split("\n")

#  print s
img = Image.new("RGB", (272, 272))
for xy in s:
    x, y = re.findall(b"\d+", xy)
    #  print x, y
    img.putpixel([int(x), int(y)], (255, 255, 255))

img = invert(img)
img.show()
#  dd if=./paintpaintpaint.jpg skip=21238 bs=1c of=xy

