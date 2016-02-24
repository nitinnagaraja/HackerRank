#!/bin/python

import sys

def answer(n, m, c):
    ldist = [sys.maxint] * n
    rdist = [sys.maxint] * n

    stations = set(c)

    distances = []

    prev_station = sys.maxint

    for i in range(n):
        if i in stations:
            prev_station = 0
        elif prev_station != sys.maxint:
            prev_station += 1
        ldist[i] = prev_station

    for i in range(n-1, -1, -1):
        if i in stations:
            prev_station = 0
        elif prev_station != sys.maxint:
            prev_station += 1
        rdist[i] = prev_station
        distances.append(min(ldist[i], rdist[i]))

    return max(distances)
    
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

print answer(n, m, c)
