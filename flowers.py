def cost(a,x):
    s=0
    for i in a:
        s+=i*(x+1)
    return s  

n, k = map(int, raw_input().split())
c = map(int, raw_input().split())

if n == k:
    print sum(c)
else:
    c = sorted(c, reverse=True)
    ans = 0
    x = 0
    for i in range(0, n, k):
        if i+k<=n:
            ans += cost(c[i:i+k], x)
        else:
            ans += cost(c[i:], x)
        x+=1
    print ans    
