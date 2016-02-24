def is_funny(a):
    n = len(a)
    r = n - 1
    for l in xrange(1, n):
        if abs(ord(a[l]) - ord(a[l-1])) != abs(ord(a[r]) - ord(a[r-1])):
            return False
        r -= 1
    return True

T = int(raw_input())
while T:
    T -= 1
    a = raw_input()
    print "Funny" if is_funny(a) else "Not Funny"
