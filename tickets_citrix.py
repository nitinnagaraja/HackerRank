n, m = map(int, raw_input().split())
a = map(int, raw_input().split())

cost = 0

while m > 0:
    max_ele = max(a)
    index = a.index(max_ele)
    cost += a[index]
    a[index] -= 1
    m -= 1
    #print a
    #print cost

print cost
