roman = {1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

def to_roman(s):
    l = len(s)

    n = int(s)
    if n in roman.keys():
        return roman[n]

    ans = ""

    while n > 0:
        l = len(s)
        c = 10 ** l
        p = 10 ** (l-1)

        if n in roman.keys():
            return ans + roman[n]

        if n >= (c - p):
            ans += roman[p]
            n += p
            c *= 10
            p *= 10

        if n >= (c/2 - p) and n < c/2:
            ans += roman[p]
            n += p

        if n in roman.keys():
            return ans + roman[n]

        if n < (c/2 - p):
            q = int(n/p)
            ans += (roman[p] * q)
            n = n - (p * q)
        else:
            ans += roman[c/2]
            n -= c/2
            
        s = str(n)

    return ans

for n in range(200, 900, 3):
    print n, "   ", to_roman(str(n))
