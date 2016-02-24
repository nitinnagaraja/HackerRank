# Enter your code here. Read input from STDIN. Print output to STDOUT

def clash(a, b, ap, bp):
    m = len(a)
    n = len(b)

    print ap, bp
    while ap < m and bp < n:
        
        if bp == n-1 or (ap < m - 1 and a[ap+1] < b[bp]):
            print "here"
            return 1
        elif ap == m - 1 or (bp < n - 1 and b[bp+1] < a[ap]):
            print "there"
            return 2
        else:
            clash(a, b, ap+1, bp+1)

    if ap >= m - 1:
        return 2
    elif bp >= n - 1:
        return 1

T = int(raw_input())

for i in xrange(T):
    a = raw_input()
    b = raw_input()
    c = ""

    m = len(a)
    n = len(b)
    
    ap = 0
    bp = 0

    for j in xrange(m+n):
        if ap < m and bp < n:
            #print ap, bp, a[ap], b[bp]
            if a[ap] < b[bp]:
                c += a[ap]
                ap += 1
            elif b[bp] < a[ap]:
                c += b[bp]
                bp += 1
            elif a[ap] == b[bp]:
                x = clash(a, b, ap, bp)
                #print j, ap, bp, x
                #x = cmp(a, b)
                if x == 1:
                    c += a[ap]
                    ap += 1
                elif x == 2:
                    c += b[bp]
                    bp += 1
                # pop from a
                #if bp == n-1 or (ap < m - 1 and a[ap+1] < b[bp]):
                #    c += a[ap]
                #    ap += 1
                # pop from b
                #elif ap == m - 1 or (bp < n - 1 and b[bp+1] < a[ap]):
                #    c += b[bp]
                #    bp += 1
        elif ap >= m-1:
            c += b[bp:]
            break
        elif bp >= n-1:
            c += a[ap:]
            break
        
        #print ap, bp, c

    print c
