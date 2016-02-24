def sol(a, x, d):
    pos = 0
    i = 0
    mydict = {}
    while i < len(a):
        
        if pos + d >= a[i] and a[i]>pos:
            pos = a[i]
            if pos + d >= x:
                return i

        if a[i] > pos + d:
            mydict[a[i]] = i

        j = pos+d
        while j <= pos+d and j > pos:
            if j in mydict.keys():
                pos = j
                j = pos+d 
                if pos + d >= x:                    
                    return i
                else:                        
                    continue    
            j -= 1
            
        i += 1

    return -1



T = 7
while T:
    a = map(int, raw_input().split())
    X = int(raw_input())
    D = int(raw_input())
    print sol(a, X, D)
    T -= 1
