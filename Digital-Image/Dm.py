#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pprint import pprint
import Queue
import pdb

class point():
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step

image = ""
vis = ""
st = ""
ed = ""

def init():
    global image, st, ed, vis

    st = (1, 3)
    ed = (1, 7)
    vis = [[0 for i in xrange(10)] for j in xrange(7)]
    
    image = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
    #  print len(image)
    #  print len(image[0])
    #  pprint(vis)
    print "The image is:"
    pprint(image)
    print "Start Point is", st
    print "End Point is", ed


def is_valid(now, m):
    if not (0 < m.x < len(image) and 0 < m.y < len(image[0])):
        return False
    elif image[m.x][m.y] == 0:
        #  pdb.set_trace()
        return False
    elif vis[m.x][m.y] == True:
        return False
    elif not is_m(now, m):
        return False
    else:
        return True


def is_m(now, m):
    if now.x == m.x and now.y + 1 == m.y:
        return True
    elif now.x == m.x and now.y - 1 == m.y:
        return True
    elif now.x + 1 == m.x and now.y == m.y:
        return True
    elif now.x - 1 == m.x and now.y == m.y:
        return True
    elif now.x - 1 == m.x and now.y - 1 == m.y and image[now.x - 1][now.y] == 0 and image[now.x][now.y - 1] == 0:
        return True
    elif now.x - 1 == m.x and now.y + 1 == m.y and image[now.x - 1][now.y] == 0 and image[now.x][now.y + 1] == 0:
        return True
    elif now.x + 1 == m.x and now.y - 1 == m.y and image[now.x][now.y - 1] == 0 and image[now.x + 1][now.y] == 0:
        return True
    elif now.x + 1 == m.x and now.y + 1 == m.y and image[now.x][now.y + 1] == 0 and image[now.x + 1][now.y] == 0:
        return True
    else:
        return False

def BFS(st, ed):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    q = Queue.Queue()
    now = point(st[0], st[1], 0)
    q.put(now)
    vis[now.x][now.y] = True 

    while not q.empty():
        now = q.get()
        if now.x == ed[0] and now.y == ed[1]:
            print "Dm between", st, "and", ed, "is %d" % now.step
            return 


        for i in xrange(8):
            next = point(now.x + dx[i], now.y + dy[i], now.step + 1)

            if is_valid(now, next):
                q.put(next)
                vis[next.x][next.y] == True

    print "There is no path between the two points"
    return 


if __name__ == "__main__":
    init()
    BFS(st, ed)
