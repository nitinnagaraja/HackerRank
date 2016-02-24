# Enter your code here. Read input from STDIN. Print output to STDOUT

def pal(a):
    n = len(a)
    l = 0
    r = n - 1
    ans1 = -1
    ans2 = -1

    x = 0
    y = 0
    
    while l < r:
        if a[l] != a[r]:
            if a[l+1] == a[r]:
                ans1 = l
            if a[r-1] == a[l]:
                ans2 = r

        if ans1 != -1 and ans2 != -1:

            # assume l is extra
            if a[ans1+2] == a[ans2-1]:
                return ans1

            # assume r is extra
            if a[ans1+1] == a[ans2-2]:
                return ans2

        elif ans1 != -1:
            return ans1
        elif ans2 != -1:
            return ans2

        l += 1
        r -= 1
    
    return -1

T = int(raw_input())

while T:
    a = raw_input()
    T -= 1
    print pal(a)
