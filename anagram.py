T=int(raw_input())
for i in range(T):
    s=raw_input()
    c=len(s)
    ans=0
    for l in range(c):     
        d={}
        for k in range(c-l):
            x=str(sorted(s[k:k+l+1]))    
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1
        for x in d.values():
            if x >= 2:
                ans+=(x*(x-1)/2)
    print ans
