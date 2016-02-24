import sys

def circles(D, r, c):
    soln = []
    for i in xrange(len(r)):
        ri = r[i]
        index = -1

        for j in xrange(len(r)):
            diff = D - ri
            if r[j] >= diff:
                if index >= 0:
                    if c[j] < c[index]:
                        index = j
                    if c[j] == c[index]:
                        if r[j] > r[index]:
                            index = j
                else:
                    index = j

        if index == -1:
            soln.append(0)
        else:
            soln.append(index + 1)

    return soln


n, D = map(int, raw_input().split())

r = map(int, raw_input().split())

c = map(int, raw_input().split())

res = circles(D, r, c)
print res
