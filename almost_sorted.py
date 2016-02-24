def reverse_segment(a):
    n = len(a)
    dec = inc = 0

    for i in range(n-1):
        if a[i+1] < a[i]:
            dec = i
            break

    for i in range(dec, n-1):
        if a[i+1] > a[i]:
            inc = i

    if a[dec] < a[inc+1]:
        return (dec + 1, inc + 1)

    print inc, dec
    if inc == 0:
        return (dec + 1, n)

    return None

def swap_possible(a):
    n = len(a)
    p1 = p2 = -1
    
    for i in range(n):
        if a[i+1] < a[i]:
            p1 = i
            break

    for i in range(p1 + 1, n - 1):
        if a[i+1] < a[i]:
            p2 = i
            break

    if p1 != -1 and p2 != -1:
        if a[p2 + 1] < a[p1 + 1] and a[p2] < a[p1]:
            if p2 + 2 >= n:
                return (p1 + 1, p2 + 2)
            elif a[p1] < a[p2 + 2]:
                return (p1 + 1, p2 + 2)

    if p1 != -1 and p2 == -1:
        if p1 == n - 2:
            return (n-1, n)
        if a[p1] < a[p1 + 2]:
            return (p1 + 1, p2 + 2)

    return None

def is_sorted(a):
    for i in xrange(len(a) - 1):
        if a[i+1] < a[i]:
            return False
    return True

n = int(raw_input())
a = map(int, raw_input().split())

if is_sorted(a):
    print "yes"
else:
    s = swap_possible(a)
    if s is not None:
        print "yes"
        print "swap", s[0], s[1]
    else:
        rev = reverse_segment(a)
        if rev is not None:
            print "yes"
            print "reverse", rev[0], rev[1]
        else:
            print "no"
