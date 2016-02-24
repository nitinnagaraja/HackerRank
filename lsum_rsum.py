def equal(a):
    l = [0] * n
    r = [0] * n
    i = 1
    j = n - 2
    
    while i < n:
        l[i] = l[i-1] + a[i-1]
        i += 1

    while j >= 0:
        r[j] = r[j+1] + a[j+1]
        j -= 1

    for i in range(0, n):
        if l[i] == r[i]:
            return 1

    return 0

T = int(raw_input())

while T:
    T -= 1
    n = int(raw_input())
    a = map(int, raw_input().split())
    print "YES" if equal(a) else "NO"
