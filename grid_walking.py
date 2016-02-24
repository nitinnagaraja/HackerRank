def no_of_ways(x, D, n, m):
    ans = 0

    if m == 0:
        return 1

    for i in xrange(n):
            x[i] += 1
            if x[i] > 0 and x[i] <= D[i]:
                ans += no_of_ways(x, D, n, m - 1)
            x[i] -= 2
            if x[i] > 0 and x[i] <= D[i]:
                ans += no_of_ways(x, D, n, m - 1)
            x[i] += 1

    return ans

T = int(raw_input())

while T:
    n, m = map(int, raw_input().split())
    X = map(int, raw_input().split())
    D = map(int, raw_input().split())

    print no_of_ways(X, D, n, m)

    T -= 1
