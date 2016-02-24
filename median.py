def median(a):
    n = len(a)
    if n % 2 == 1:
        return a[n/2]
    else:
        return (a[n/2] + a[n/2 - 1])/2

def find_median(a, b):
    m1 = 0
    m2 = 0
    n = len(a)

    if n < 1:
        return -1

    if n == 1:
        print a, b
        return (a[0] + b[0])/2

    if n == 2:
        print a, b
        return ((max(a[0], b[0]) + min(a[1], b[1]))/2)

    m1 = median(a)
    m2 = median(b)

    if m1 == m2:
        return m1

    if m1 < m2:
        if n % 2 == 0:
            return find_median(a[n/2 - 1:], b[:n/2])
        else:
            return find_median(a[n/2 + 1:], b[:n/2])
    else:
        if n % 2 == 0:
            return find_median(b[n/2 - 1:], a[:n/2])
        else:
            return find_median(b[n/2:], a[:n/2])
    

a = map(int, raw_input().split())
b = map(int, raw_input().split())

median = find_median(a, b)
print "Median =", median
