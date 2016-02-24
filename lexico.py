def swap(s, i, j):
    l = list(s);
    l[i], l[j] = l[j], l[i]
    return ''.join(l)

T = int(raw_input())

while T:
    T -= 1
    a = raw_input()

    n = len(a)
    i = n-1
    done = False

    while i > 1:
        if a[i] > a[i-1]:
            a = swap(a, i, i-1)
            done = True
            break
        i -= 1

    s = ''
    if done:
        print a
    else:
        c = a[0]
        b = sorted(a)
        i = 0
        res = []
        while i < n:
            if b[i] > c:
                s = ''.join(b[i])
                s += ''.join(b[:i])
                s += ''.join(b[i+1:])
                print s
                break
            i += 1

        if s == '':
            print "no answer"
