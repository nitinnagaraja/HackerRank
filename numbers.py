n = int(raw_input())
a = map(int, raw_input().split())

s = int(raw_input())
q = map(int, raw_input().split())

for i in xrange(s):
    res = 0
    for j in xrange(n):    
        add = a[j] + q[i]
        if add >= 0:
            res += add
        else:
            res -= add
        a[j] = add
        #print res
        #print a
    print res
