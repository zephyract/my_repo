#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

bacon = "ABAAAABBABBAABBAABAABAAABAABAABAABABAABBABAAAABBABAABBAAAABAABBBAAAABBABAAAABBABAABBA"
aaencode = ""
for i in bacon:
    aaencode += "flag" if i == "A" else "Flag"

#  print aaencode
with open("cipher", "w") as f:
    f.write(aaencode)
