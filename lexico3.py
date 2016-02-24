def swap(s, i, j):
    l = list(s);
    l[i], l[j] = l[j], l[i]
    return ''.join(l)


def lexico(s):
    n = len(s)
    a = [0] * (n - 1)

    i = 0
    while i < n-1:
        a[i] = ord(s[i]) - ord(s[i+1])
        i += 1

    left = -1
    i = n - 2
    while i >= 0:
        if a[i] < 0:
            left = i
            break
        i -= 1

    if left == -1:
        print "no answer"
        return

    i = left+1
    add = a[left]
    right = left + 1

    #print a
    #print add
    
    while i < n-1:
        add += a[i]
        if add >= 0:
            right = i
            break
        if i == n - 2:
            right = i + 1
        i += 1

    #print s
    #print left, right
    s = swap(s, left, right)

    #print "after swap"
    #print s

    s2 = ''.join(sorted(s[left+1:]))
    print s[:left+1] + s2
    
T = int(raw_input())

while T:
    T -= 1
    s = raw_input()
    lexico(s)
