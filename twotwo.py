import math

def count_sub(s, sb):
    results = 0
    sub_len = len(sb)
    l = len(s)
    for i in range(l - sub_len + 1):
        if s[i:i+sub_len] == sb:
            results += 1
    return results

T = int(raw_input())

while T:
    a = raw_input()
    T -= 1
    n = int(a)
    exp = int(math.log(n, 2))
    ans = 0
    x = 0
    for i in xrange(exp+1):
        x = pow(2, i)
        x = str(x)
        ans += count_sub(a, x)
    print ans
