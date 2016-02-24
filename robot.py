# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

while T:
    m, n = map(int, raw_input().split())
    dist = 0
    r1 = -1
    r2 = -1

    a, b = map(int, raw_input().split())
    
    for i in xrange(n):
        if i != n-1:
            nexta, nextb = map(int, raw_input().split())
        
        if r1 == -1:
            dist = dist + abs(b - a)
            r1 = b
            print "r1,"
            
        elif r2 == -1:
            if abs(r1 - a) < abs(nexta - b):
                dist = dist + abs(r1 - a) + abs(a - b)
                r1 = b
                print "r1,"
            else:
                dist = dist + abs(b - a)
                r2 = b
                print "r2,"
        else:
            if abs(r1 - a) <= abs(r2 - a):
                dist = dist + abs(r1 - a) + abs(a - b)
                r1 = b
                print "r1,"
            else:
                dist = dist + abs(r2 - a) + abs(a - b)
                r2 = b
                print "r2,"
        #print a, b, r1, r2, dist
        a, b = nexta, nextb

    T -= 1
    print dist
