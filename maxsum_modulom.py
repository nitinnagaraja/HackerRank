def subArraySum(a, s):
    #print s
    cur = a[0]
    start = 0

    for i in range(1, n+1):
        while(cur > s and start < i-1):
            cur -= a[start]
            start += 1

        if cur == s:
            #print a[start:i]
            print sum(a[start:i])
            return 1

        if i < n:
            cur += a[i]

    return 0

def maxsum_moduloM(a, m):
    mysum = sum(a)
    q = mysum/m
    prev = (q - 1) * m
    k = prev + (m - 1)
    #print mysum, q, prev, k
    while k > prev:
        if subArraySum(a, k - prev):
            return 1
        k -= 1
    return 0

T = int(raw_input())
while T:
    T -= 1
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    maxsum_moduloM(a, m)
