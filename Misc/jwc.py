#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import requests
from sys import argv
from time import sleep

headers = {
        'Referer': 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk',
        'Cookie': argv[1]
    }


while True:
    try:
        for i in range(1, len(argv)):
            print i
            url = 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/ggxxkxkOper/jx0404id=%s&xkzy=&trjf=' % argv[i]
            r = requests.get(url = url, headers = headers)
            if "true" in r.content:
                print "success"
                break
        sleep(1)
    except:
        pass
