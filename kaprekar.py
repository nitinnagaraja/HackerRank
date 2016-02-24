l = int(raw_input())
r = int(raw_input())

res = []

for i in xrange(l, r+1):
    sq = (i * i)
    d = len(str(i))
    n = len(str(sq))
    s1 = str(sq)[:n-d]
    s2 = str(sq)[n-d:]
    l2 = len(s2)
    l1 = len(s1)
    if l1 == 0:
        if int(s2) == i:
            res.append(i)
    elif (int(s1) + int(s2)) == i:
        res.append(i)

if len(res) == 0:
    print "INVALID RANGE"
else:
    for num in res:
        print num,
