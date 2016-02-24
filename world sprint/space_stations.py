#!/bin/python

import sys

def max_nearest_space_station(n, m, c):
    distances = []
    a = [x for x in range(n) if x not in c]

    if not a:
        return 0

    max_c = max(c)
    min_c = min(c)

    if a[-1] < min_c:
        return c[-1] - a[0]
    elif a[0] > max_c:
        return a[-1] - c[0]
            
    for i in a:
        if i < min_c:
            val = min_c - i
        elif i > max_c:
            val = i - max_c
        else:
            temp = [abs(i - ci) for ci in c]
            val = min(temp)
        distances.append(val)
    return max(distances) if distances else 0

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

print max_nearest_space_station(n, m, c)
