# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

a = map(int, raw_input().split())

a.sort()

b = [0] * (n-1)

for i in xrange(n-1):
    b[i] = abs(a[i] - a[i+1])
    
mindiff = min(b)

for i in xrange(n-1):
    if abs(a[i] - a[i+1]) == mindiff:
        print a[i], a[i+1], 
