import sys
from itertools import combinations

def answer(d, n):
    ans = 0
    for item in combinations(range(n), 2):
        x = item[0]
        y = item[1]
        

T = int(raw_input())

while T:
    n, m = map(int, raw_input().split())
    d = [[sys.maxint for i in range(n)] for j in range(n)]
    while m:
        a, b, c = map(int, raw_input().split())
        d[a-1][b-1] = d[b-1][a-1] = c
        m -= 1
    T -= 1

    print answer(d, n)
