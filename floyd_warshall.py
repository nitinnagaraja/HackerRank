from sys import maxint

def floyd_warshall(dist):
    n = len(dist)
    for i in range(n):
        for j in range(n):
            if dist[j][i] is None: continue
            for k in range(n):
                if dist[i][k] is None: continue
                if dist[j][i] + dist[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

    return dist

n, m = map(int, raw_input().split())

dist =  [[None] * n for _ in range(n)]

for i in xrange(m):
    a, b, d = map(int, raw_input().split())
    dist[a-1][b-1] = d

for i in xrange(n):
    dist[i][i] = 0

#print dist

new_dist = floyd_warshall(dist)

q = int(raw_input())

for i in xrange(q):
    a, b = map(int, raw_input().split())
    print -1 if new_dist[a-1][b-1] is None else new_dist[a-1][b-1]
