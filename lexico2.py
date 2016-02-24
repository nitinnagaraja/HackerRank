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

    while i > 0:
        if a[i] > a[i-1]:
            a = swap(a, i, i-1)
            done = True
            break
        i -= 1

    print a
