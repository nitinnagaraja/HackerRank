import sys

def circles(D, r, c):
    soln = [0] * 5
    hm = {}
    for i in xrange(len(r)):
        hm[r[i]] = i

    sl = []
    
    for i in xrange(len(r)):
        sl.append((r[i], c[i], i))

    sl = sorted(sl, key = lambda x: x[0])
    
    costs = []

    n = len(r)

    i = 0
    j = n-1
    poss = []
    
    while i < n and j >= 0:
        if r[i] + r[j] >= D:
            poss.append(sl[j][2])
            j -= 1
            print poss
            continue

        if len(poss) == 0:
            ret = 0
        else:
            costs = []
            for k in xrange(len(poss)):
                costs.append((c[poss[k]],poss[k]))

 
            mincost = (min(costs, key=lambda x: x[0]))[0]
            best_costs = []
            for k in xrange(len(poss)):
                if costs[k][0] == mincost:
                    best_costs.append(costs[k][1])

            radius = r[best_costs[0]]
            ret = best_costs[0]
            for k in xrange(len(best_costs)):
                if r[k] == radius:
                    ret = k
                else:
                    break

        if ret == 0:
            soln[sl[i][2]] = ret
        else:
            soln[sl[i][2]] = ret + 1

        if ret != 0:
            poss.append(ret)

        print poss
        print "\n"
        
        i += 1

    return soln


n, D = map(int, raw_input().split())

r = map(int, raw_input().split())

c = map(int, raw_input().split())

res = circles(D, r, c)
print res
