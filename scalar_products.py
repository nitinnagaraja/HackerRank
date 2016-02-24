# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

while T:
    m, n = map(int, raw_input().split())
    dist = 0
    r1 = 0
    r2 = 0

    for i in xrange(n):
        a, b = map(int, raw_input().split())
        
        if i == 0:
            dist = dist + abs(b - a)
            r1 = b
            
        elif i == 1:
            dist = dist + abs(b - a)
            r2 = b
        
        else:
            if abs(r1 - a) <= abs(r2 - a):
                dist = dist + abs(r1 - a) + abs(a - b)
                r1 = b
            else:
                dist = dist + abs(r1 - a) + abs(a - b)
                r2 = b

        print a, b, r1, r2, dist

    T -= 1
    print dist
